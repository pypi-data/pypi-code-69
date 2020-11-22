import copy
from typing import Optional, Mapping, List, Sequence, Union, Dict

from .config import Config
from .data import ChartData
from .exception import ConfigurationError
from .resource import is_list_resource


class Processor:
    """
    Processor filters and mutates charts and its objects.
    """
    def filter(self, chart: 'Chart', data: ChartData) -> bool:
        """
        Filters chart objects.

        :param chart: original chart
        :param data: chart object data
        :return: True to include the object, False to exclude it
        """
        return True

    def mutateBefore(self, chart: 'Chart', data: ChartData) -> None:
        """
        Mutate chart object before filtering.

        :param chart: original chart
        :param data: chart object data
        """
        pass

    def mutate(self, chart: 'Chart', data: ChartData) -> None:
        """
        Mutate chart object after filtering.

        :param chart: original chart
        :param data: chart object data
        """
        pass

    def mutateComplete(self, chart: 'Chart', data: Sequence[ChartData]) -> Optional[Sequence[ChartData]]:
        """
        Mutate complete chart objects after all other processing.

        :param chart: original chart
        :param data: list of chart object data
        :returns: if not None, replaces the complete chart object data with the result, otherwise keep
            the current value.
        """
        return None


class ProcessorChain(Processor):
    """
    A processor for chaining multiple :class:`Processor`.

    :param processor: list of :class:`Processor`.
    """
    processors: Sequence[Processor]

    def __init__(self, *processor: Processor):
        self.processors = processor

    def filter(self, chart: 'Chart', data: ChartData) -> bool:
        for p in self.processors:
            if not p.filter(chart, data):
                return False
        return True

    def mutateBefore(self, chart: 'Chart', data: ChartData) -> None:
        for p in self.processors:
            p.mutateBefore(chart, data)

    def mutate(self, chart: 'Chart', data: ChartData) -> None:
        for p in self.processors:
            p.mutate(chart, data)

    def mutateComplete(self, chart: 'Chart', data: Sequence[ChartData]) -> Optional[Sequence[ChartData]]:
        lastdata = data
        for p in self.processors:
            pret = p.mutateComplete(chart, lastdata)
            if pret is not None:
                lastdata = pret
        return lastdata


SplitterCategoryFuncResult = Optional[Union[bool, str, Sequence[str]]]
"""
The :class:`Splitter` categorization function.

The possible return types are:

- ```bool```: True includes the object in ALL categories, False in none
- ```str```: includes the object only in this category
- ```Sequence[str]```: includes the object in the list of categories
- ```None```: inconclusive. If using :class:`SplitterChain`, skip to next splitter, otherwise means
    the same as False
"""


class Splitter:
    """
    Chart splitter configuration.

    Use this to split chart objects in different categories.

    It is possible for a chart object to appear in more than one category, depending on the
    splitter configuration.
    """
    def category(self, chart: 'Chart', categories: Sequence[str], data: ChartData) -> SplitterCategoryFuncResult:
        """
        Returns the categories that the chart object should be added to.

        :param chart: original chart
        :param categories: available categories
        :param data: chart data
        :return: splitter category result. See  :data:`SplitterCategoryFuncResult` for details.
        """
        return True


class SplitterChain(Splitter):
    """
    A splitter for chaining multiple :class:`Splitter`.

    :param splitters: list of :class:`Splitter`.
    """
    splitters: Sequence[Splitter]

    def __init__(self, *splitters: Splitter):
        self.splitters = splitters

    def category(self, chart: 'Chart', categories: Sequence[str], data: ChartData) -> SplitterCategoryFuncResult:
        """
        Returns the categories that the chart object should be added to.

        The next splitter in the chain is only called when a splitter returns None. The first one that returns
        non-None will be the returned value.
        """
        for s in self.splitters:
            sr = s.category(chart, categories, data)
            if sr is not None:
                return sr
        return None


class Chart:
    """
    Chart represents a set of object Kubernetes.

    :param config: Config
    :param data: Initial data
    """
    config: Config
    data: List[ChartData]
    """List of objected generated from the Helm chart"""

    def __init__(self, config: Optional[Config] = None, data: Optional[Sequence[ChartData]] = None):
        self.config = config if config is not None else Config()
        self.data = []
        if data is not None:
            self.data.extend(data)

    def createClone(self) -> 'Chart':
        """
        Create a clones of current chart. The data should NOT be copied.

        :return: a clone of the current :class:`Chart` class
        """
        return Chart(self.config)

    def clone(self, clone_data: bool = True) -> 'Chart':
        """
        Clones the current chart.

        :param clone_data: whether to also clone data
        :return: a clone of the current :class:`Chart` class
        """
        ret = self.createClone()
        if clone_data:
            ret.data = copy.deepcopy(self.data)
        return ret

    def process(self, processor: Optional[Processor]) -> 'Chart':
        """
        Process the current chart using the processor and return a new :class:`Chart` instance if
        a processor was passed, otherwise returns the same instance.

        The source :class:`Chart` remains unchanged in case of processing.

        :param processor: the :class:`Processor` to apply. If None, returns the same instance unchanged.
        :return: a processed :class:`Chart` instance, or the same instance if *processor* is None.
        """
        if processor is None:
            return self

        ret = self.clone(clone_data=False)
        for d in self.data:
            newd = copy.deepcopy(d)
            if self.config.parse_list_resource and is_list_resource(newd):
                # https://github.com/kubernetes/kubectl/issues/837
                newditems: List[ChartData] = []
                if 'items' in newd:
                    for newditem in newd['items']:
                        processor.mutateBefore(self, newditem)
                        if not processor.filter(self, newditem):
                            continue
                        processor.mutate(self, newditem)
                        newditems.append(newditem)
                if len(newditems) == 0:
                    continue
                newd['items'] = newditems
            else:
                processor.mutateBefore(self, newd)
                if not processor.filter(self, newd):
                    continue
                processor.mutate(self, newd)
            ret.data.append(newd)

        newdata = processor.mutateComplete(self, ret.data)
        if newdata is not None:
            ret.data = []
            ret.data.extend(newdata)

        return ret

    def split(self, categories: List[str], splitter: Splitter) -> Mapping[str, 'Chart']:
        """
        Splits the chart objects in a list of categories.

        Returns new :class:`Chart` instances, the source :class:`Chart` remains unchanged.

        :param categories: list of categories to split.
        :param splitter: the splitter to use to categorize the objects.
        :return: a ```Mapping``` of categories and their charts
        :raises ConfigurationError: on a category that not exists
        """
        ret: Dict[str, 'Chart'] = {}

        for cname in categories:
            ret[cname] = self.clone(clone_data=False)

        for d in self.data:
            category = splitter.category(self, categories, d)
            categorylist: Optional[Sequence[str]] = None
            if category is True:
                categorylist = list(categories)
            elif isinstance(category, str):
                categorylist = [category]
            elif isinstance(category, Sequence):
                categorylist = category

            if categorylist is not None:
                for cname in categorylist:
                    if cname not in categories:
                        raise ConfigurationError('Unknown category: {}'.format(cname))
                    ret[cname].data.append(copy.deepcopy(d))

        return ret

    def sort(self) -> 'Chart':
        """
        Sort resource list by resource name, but without changing overall resource kind sorting
        """
        out = []
        tmp = []
        last_kind = None
        for r in self.data:
            kind = r['kind']
            if last_kind and kind != last_kind:
                out += sorted(tmp, key=lambda r: r['metadata']['name'])
                tmp = []
            tmp.append(r)
            last_kind = kind
        out += sorted(tmp, key=lambda r: r['metadata']['name'])
        self.data = out

        return self
