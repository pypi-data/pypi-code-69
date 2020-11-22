"""
Task implementations

A Task is a unit of work that produces a persistent change (Product)
such as a bash or a SQL script
"""
import shlex
import subprocess
import pdb

from IPython.terminal.debugger import TerminalPdb, Pdb

from ploomber.tasks.Task import Task
from ploomber.sources import (PythonCallableSource, GenericSource, EmptySource)
from ploomber.clients import ShellClient
from ploomber.products.Metadata import MetadataAlwaysUpToDate
from ploomber.exceptions import TaskBuildError
from ploomber.constants import TaskStatus
from ploomber.sources.interact import CallableInteractiveDeveloper
from ploomber.tasks.Params import Params


class PythonCallable(Task):
    """
    Run a Python callable (e.g. a function)

    Parameters
    ----------
    source: callable
        The callable to execute
    product: ploomber.products.Product
        Product generated upon successful execution
    dag: ploomber.DAG
        A DAG to add this task to
    name: str
        A str to indentify this task. Should not already exist in the dag
    params: dict
        Parameters to pass to the callable, by default, the callable will
        be executed with a "product" (which will contain the product object).
        It will also include a "upstream" parameter if the task has upstream
        dependencies along with any parameters declared here
    unserializer: callable, optional
        A callable to unserialize upstream products, the product object
        is passed as unique argument. If None, the source function receives
        the product object directly. If the task has no upstream dependencies,
        this argument has no effect
    serializer: callable, optional
        A callable to serialize this task's product, must take two arguments,
        the first argument passed is the value returned by the task's
        source, the second argument is the product oject. If None, the
        task's source is responsible for serializing its own product
    """
    def __init__(self,
                 source,
                 product,
                 dag,
                 name=None,
                 params=None,
                 unserializer=None,
                 serializer=None):
        kwargs = dict(hot_reload=dag._params.hot_reload)
        self._source = type(self)._init_source(source, kwargs)
        self._serializer = serializer or dag.serializer
        self._unserializer = unserializer or dag.unserializer
        super().__init__(product, dag, name, params)

    @staticmethod
    def _init_source(source, kwargs):
        return PythonCallableSource(source, **kwargs)

    def run(self):
        params = self.params.to_dict()

        # unserialize upstream dependencies if needed
        if 'upstream' in params and self._unserializer:
            params['upstream'] = {
                k: self._unserializer(v)
                for k, v in params['upstream'].items()
            }

        # call function
        out = self.source.primitive(**Params._from_dict(params, copy=False))

        # serialize output if needed
        if self._serializer:
            if out is None:
                raise ValueError('Callable {} must return a value if task '
                                 'is initialized with a serializer'.format(
                                     self.source.primitive))
            else:
                self._serializer(out, params['product'])

    def develop(self, app='notebook', args=None):
        """Edit function interactively using Jupyter

        Parameters
        ----------
        app : str, {'notebook', 'lab'}, default='notebook'
            Which jupyter application to use

        args : str
            Extra args passed to the selected jupyter application

        Notes
        -----
        Be careful when developing tasks interacively. If the task has run
        successfully, you overwrite products but don't save the
        updated source code, your DAG will enter an inconsistent state where
        the metadata won't match the overwritten product.
        """
        apps = {'notebook', 'lab'}

        if app not in apps:
            raise ValueError('"app" must be one of {}, got: "{}"'.format(
                apps, app))

        if self.exec_status == TaskStatus.WaitingRender:
            raise TaskBuildError(
                'Error in task "{}". '
                'Cannot call task.develop() on a task that has '
                'not been '
                'rendered, call DAG.render() first'.format(self.name))

        # TODO: Params should implement an option to call to_json_serializable
        # on product to avoid repetition I'm using this same code in notebook
        # runner. Also raise error if any of the params is not
        # json serializable
        # TODO: resolve to absolute to make relative paths work
        params = self.params.to_json_serializable()
        params['product'] = params['product'].to_json_serializable()

        with CallableInteractiveDeveloper(self.source.primitive,
                                          params) as tmp:
            try:
                subprocess.run(['jupyter', app, tmp] + shlex.split(args or ''),
                               check=True)
            except KeyboardInterrupt:
                print(f'Jupyter {app} application closed...')

    def debug(self, kind='ipdb'):
        """
        Run callable in debug mode.

        Parameters
        ----------
        kind : str ('ipdb' or 'pdb')
            Which debugger to use 'ipdb' for IPython debugger or 'pdb' for
            debugger from the standard library

        Notes
        -----
        Be careful when debugging tasks. If the task has run
        successfully, you overwrite products but don't save the
        updated source code, your DAG will enter an inconsistent state where
        the metadata won't match the overwritten product.
        """
        opts = {'ipdb', 'pdb'}

        if kind not in opts:
            raise ValueError('"kind" must be one of {}, got: "{}"'.format(
                opts, kind))

        if self.exec_status == TaskStatus.WaitingRender:
            raise TaskBuildError('Error in task "{}". '
                                 'Cannot call task.debug() on a task that has '
                                 'not been '
                                 'rendered, call DAG.render() first'.format(
                                     self.name))
        if kind == 'ipdb':
            try:
                # this seems to only work in a Terminal
                ipdb = TerminalPdb()
            except AttributeError:
                # this works in a Jupyter notebook
                ipdb = Pdb()

            ipdb.runcall(self.source.primitive, **self.params)
        elif kind == 'pdb':
            pdb.runcall(self.source.primitive, **self.params)


class ShellScript(Task):
    """Execute a shell script in a shell

    Parameters
    ----------
    source: str or pathlib.Path
        Script source, if str, the content is interpreted as the actual
        script, if pathlib.Path, the content of the file is loaded. The
        souce code must have the {{product}} tag
    product: ploomber.products.Product
        Product generated upon successful execution
    dag: ploomber.DAG
        A DAG to add this task to
    name: str
        A str to indentify this task. Should not already exist in the dag
    client: ploomber.clients.ShellClient or RemoteShellClient, optional
        The client used to connect to the database. Only required
        if no dag-level client has been declared using dag.clients[class]
    params: dict, optional
        Parameters to pass to the script, by default, the callable will
        be executed with a "product" (which will contain the product object).
        It will also include a "upstream" parameter if the task has upstream
        dependencies along with any parameters declared here. The source
        code is converted to a jinja2.Template for passing parameters,
        refer to jinja2 documentation for details
    """
    def __init__(self,
                 source,
                 product,
                 dag,
                 name=None,
                 client=None,
                 params=None):
        kwargs = dict(hot_reload=dag._params.hot_reload)
        self._source = type(self)._init_source(source, kwargs)
        super().__init__(product, dag, name, params)

        self.client = client or self.dag.clients.get(type(self))

        if self.client is None:
            self.client = ShellClient()

    @staticmethod
    def _init_source(source, kwargs):
        required = {
            'product': ('ShellScript must include {{product}} in '
                        'its source')
        }

        return GenericSource(source, **kwargs, required=required)

    def run(self):
        self.client.execute(str(self.source))


class DownloadFromURL(Task):
    """
    Download a file from a URL (uses urllib.request.urlretrieve)

    Parameters
    ----------
    source: str
        URL to download the file from
    product: ploomber.products.File
        Product generated upon successful execution
    dag: ploomber.DAG
        A DAG to add this task to
    name: str
        A str to indentify this task. Should not already exist in the dag
    """
    def __init__(self, source, product, dag, name=None, params=None):
        params = params or {}
        kwargs = dict(hot_reload=dag._params.hot_reload)
        self._source = type(self)._init_source(source, kwargs)
        super().__init__(product, dag, name, params)

    def run(self):
        # lazily load urllib as it is slow to import
        from urllib import request
        request.urlretrieve(str(self.source), filename=str(self.product))

    @staticmethod
    def _init_source(source, kwargs):
        return GenericSource(str(source), **kwargs, optional=['product'])


# TODO: move this and _Gather to helpers.py (actually create a module
# for partitioned execution)
class _Partition(Task):
    def __init__(self, product, dag, name):
        kwargs = dict(hot_reload=dag._params.hot_reload)
        self._source = type(self)._init_source(kwargs)
        super().__init__(product, dag, name, None)

    def run(self):
        """This Task does not run anything
        """
        # TODO: verify that this task has only one upstream dependencies
        # is this the best place to check?
        pass

    def _init_source(self, kwargs):
        return EmptySource(None, **kwargs)


class _Gather(PythonCallable):
    def run(self):
        pass


class Link(Task):
    """
    A dummy Task used to "plug" an external Product to a pipeline, this
    task is always considered up-to-date

    The purpose of this Task is to link a pipeline to an external read-only
    file, this task does not do anything on the dataset and the product is
    always considered up-to-date. There are two primary use cases:
    when the raw data is automatically uploaded to a file (or table) and the
    pipeline does not have control over data updates, this task can be used
    to link the pipeline to that file, without having to copy it, downstream
    tasks will see this dataset as just another Product. The second use case
    is when developing a prediction pipeline. When making predictions on new
    data, the pipeline might rely on existing data to generate features,
    this task can be used to point to such file it can also be used to
    point to a serialized model, this last scenario is only recommended
    for prediction pipeline that do not have strict performance requirements,
    unserializing models is an expensive operation, for real-time predictions,
    the model should be kept in memory

    Parameters
    ----------
    product: ploomber.products.Product
        Product to link to the dag
    dag: ploomber.DAG
        A DAG to add this task to
    name: str
        A str to indentify this task. Should not already exist in the dag
    """
    def __init__(self, product, dag, name):
        kwargs = dict(hot_reload=dag._params.hot_reload)
        self._source = type(self)._init_source(kwargs)
        super().__init__(product, dag, name, None)

        # patch product's metadata
        self.product.metadata = MetadataAlwaysUpToDate()
        # product's code will never be considered outdated
        self.product._outdated_code_dependency = self._false

        if not self.product.exists():
            raise RuntimeError('Link tasks should point to Products that '
                               'already exist. "{}" task product "{}" does '
                               'not exist'.format(self.name, self.product))

    def run(self):
        pass

    def set_upstream(self, other):
        raise RuntimeError('Link tasks should not have upstream dependencies')

    @staticmethod
    def _init_source(kwargs):
        return EmptySource(None, **kwargs)

    def _false(self):
        # this should be __false but we can't due to
        # https://bugs.python.org/issue33007
        return False


class Input(Task):
    """
    A dummy task used to represent input provided by the user, it is always
    considered outdated.

    When making new predictions, the user must submit some input data to build
    features and then feed the model, this task can be used to point to
    such input. It does not perform any processing (read-only data) but it is
    always considered outdated, which means it will always trigger execution.

    Parameters
    ----------
    product: ploomber.products.Product
        Product to to serve as input to the dag
    dag: ploomber.DAG
        A DAG to add this task to
    name: str
        A str to indentify this task. Should not already exist in the dag
    """
    def __init__(self, product, dag, name):
        kwargs = dict(hot_reload=dag._params.hot_reload)
        self._source = type(self)._init_source(kwargs)
        super().__init__(product, dag, name, None)

        # do not save metadata (Product's location is read-only)
        self.product.metadata.update = self._null_update_metadata

        # the product will always be considered outdated
        self.product._outdated_data_dependencies = self._true
        self.product._outdated_code_dependency = self._true

        if not self.product.exists():
            raise RuntimeError('Input tasks should point to Products that '
                               'already exist. "{}" task product "{}" does '
                               'not exist'.format(self.name, self.product))

    def run(self):
        pass

    def set_upstream(self, other):
        raise RuntimeError('Input tasks should not have upstream '
                           'dependencies')

    @staticmethod
    def _init_source(kwargs):
        return EmptySource(None, **kwargs)

    def _null_update_metadata(self, metadata):
        # this should be __null_update_metadata but we can't due to
        # https://bugs.python.org/issue33007
        pass

    def _true(self):
        # this should be __true but we can't due to
        # https://bugs.python.org/issue33007
        return True
