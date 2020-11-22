# Simulation "lab notebook" for collecting results, in-memory version
#
# Copyright (C) 2016--2020 Simon Dobson
#
# This file is part of epyc, experiment management in Python.
#
# epyc is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# epyc is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with epyc. If not, see <http://www.gnu.org/licenses/gpl.html>.

from epyc import Experiment, ResultSet, ResultsDict
from pandas import DataFrame                               # type: ignore
from contextlib import contextmanager
from typing import List, Set, Dict, Any, Optional, Final

                    
class LabNotebook(object):
    '''A "laboratory notebook" collecting together the results obtained from
    different sets of experiments. A notebook is composed of :class:`ResultSet` objects,
    which are homogeneous collections of results of experiments performed at different values
    for the same set of parameters. Each result set is tagged for access,
    with the notebook using one result set as "current" at any time.

    The notebook collects together pending results from all result sets so that they
    can be accessed uniformly. This is used by labs to resolve pending results if
    there are multiple sets of experiments running simultaneously.

    :param name: (optional) the notebook name (may be meaningful for sub-classes)
    :param description: (optional) a free text description'''
 
    # Defaults
    DEFAULT_RESULTSET : Final[str] = 'epyc.resultset.default'  #: Tag for the default result set.

    def __init__(self, name : str =None, description : str =None):
        if description is None:
            description = 'A notebook' 
        self._name : Optional[str] = name                    # name
        self._description : str = description                # description
        self._resultSets: Dict[str, ResultSet] = dict()      # tag to result set
        self._resultSetTags : Dict[ResultSet, str] = dict()  # result set to tag
        self._pending : Dict[str, ResultSet] = dict()        # pending results job ids to result sets

        # add a result set with the default tag, and make it current
        defrc = self.addResultSet(self.DEFAULT_RESULTSET)
        self._current : ResultSet = defrc
        #defrc.dirty(False)                  # default shouldn't trigger a write


    # ---------- Access ----------

    def name(self) -> Optional[str]:
        """Return the name of the notebook. If the notebook is persistent,
        this likely relates to its storage in some way (for example a
        file name).

        :returns: the notebook name or None"""
        return self._name

    def description(self) -> str:
        """Return the free text description of the notebook.

        :returns: the notebook description"""
        return self._description

    def setDescription(self, d : str):
        '''Set the free text description of the notebook.

        :param d: the description'''
        self._description = d


    # ---------- Persistence ----------

    def isPersistent(self) -> bool:
        """By default notebooks are not persistent.

        :returns: False"""
        return False

    def commit(self):
        """Commit to persistent storage. By default does nothing. This should
        be called periodically to save intermediate results: it may happen
        automatically in some sub-classes, depending on their implementation."""
        pass


    # ---------- Managing results sets ----------

    def addResultSet(self, tag : str, description : str =None) -> ResultSet:
        '''Start a new experiment. This creates a new result set to hold
        the results, which will receive any results and notes.

        :param tag: unique tag for this result set
        :param: (optional) free text description of the result set
        :returns: the result set'''
        rs = ResultSet(description)
        self._resultSets[tag] = rs
        self._resultSetTags[rs] = tag
        self._current = rs
        return self._current

    def resultSets(self) -> List[str]:
        '''Return the tags for all the result sets in this notebook.

        :returns: a list of keys'''
        return list(self._resultSets.keys())

    def resultSet(self, tag : str) -> ResultSet:
        '''Return the tagged result set.

        :param tag: the tag
        :returns: the result set'''
        return self._resultSets[tag]

    def resultSetTag(self, rs : ResultSet) -> str:
        '''Return the tag associated with the given result set.

        :param rs: the result set
        :returns: the tag'''
        return self._resultSetTags[rs] 

    def select(self, tag: str) -> ResultSet:
        '''Select the given result set as current. Sub-classes may use this
        to manage memory, for example by swapping-out non-current result sets.

        :param tag: the tag
        :returns: the result set'''
        self._current = self._resultSets[tag] 
        return self._current

    def current(self) -> ResultSet:
        '''Return the current result set.

        :returns: the result set'''
        return self._current

    def currentTag(self) -> str:
        '''Return the tag of the current result set.

        :returns: the tag'''
        return self._resultSetTags[self._current]

    def numberOfResultSets(self) -> int:
        '''Return the number of result sets in this notebook.

        :returns: the numbernof result sets'''
        return len(self._resultSets)

    def __len__(self) -> int:
        '''Return the number of result sets in this notebook.
        Same as :meth:`numberOfResultSets`.

        :returns: the numbernof result sets'''
        return self.numberOfResultSets()


    # ---------- Managing pending results in the current result set ----------

    def addPendingResult(self, params : Dict[str, Any], jobid : str, tag : str =None):
        '''Add a pending result for the given point in the parameter space
        under the given job identifier to the current result set. The identifier
        will generally be meaningful to the lab that submitted the request, and
        must be unique.

        :param params: the experimental parameters
        :param jobid: the job id
        :param tag: (optional) the tag of the result set receiving the pending result (defaults to the current result set)'''
        if tag is None:
            rs = self._current
        else:
            rs = self._resultSets[tag]

        # add the pending job to the result set
        rs.addSinglePendingResult(params, jobid)

        # record the result set that holds the given job
        self._pending[jobid] = rs


    # ---------- Resolving and cancelling results in any result set ----------

    def resolvePendingResult(self, rc : ResultsDict, jobid : str):
        '''Resolve the pending result with the given job id with the given
        results dict. The experimental parameters of the result are sanity-checked
        against what the result set expected for that job.

        The result may not be pending within the current result set, but can
        be within any result set in the notebook. This will not affect
        the result set that is selected as current.

        :param rc: the results dict
        :param jobid: the job id'''
        tag = self._resultSetTags[self._pending[jobid]]
        self.addResult(rc, tag=tag)
        self.cancelPendingResult(jobid)
 
    def cancelPendingResult(self, jobid : str):
        '''Cancel the given pending result.

        The result may not be pending within the current result set, but can
        be within any result set in the notebook. This will not affect
        the result set that is selected as current.

        :param jobid: the job id'''

        # find the result set for the job
        rs = self._pending[jobid]

        # resolve this result
        rs.cancelSinglePendingResult(jobid)

        # mark the job as resolved with the notebook
        del self._pending[jobid] 
            
    def ready(self, tag : str =None) -> bool:
        '''Test whether the result set has pending results. 

        :params tag: (optional) the result set tag (defaults to the current set)
        :returns: True if all pending results have been resolved (or cancelled)'''
        if tag is None:
            rs = self._current
        else:
            rs = self._resultSets[tag]
        return rs.ready()

    def readyFraction(self, tag : str =None) -> float:
        """Test what fraction of results are available in the tagged result set.
        
        :params tag: (optional) the result set tag (defaults to the current set)
        :returns: the fraction of available results"""
        if tag is None:
            rsc = self._current
        else:
            rsc = self._resultSets[tag]
        rsc = self.current()
        nr = rsc.numberOfResults()
        np = rsc.numberOfPendingResults()
        tr = nr + np
        if tr == 0:
            return 1.0
        else:
            return nr / tr

    def pendingResults(self, tag : str =None) -> List[str]:
        '''Return the identifiers of the results pending in the tagged dataset.
        
        :params tag: (optional) the result set tag (defaults to the current set)
        :returns: a set of job identifiers'''
        if tag is None:
            rs = self._current
        else:
            rs = self._resultSets[tag]
        return rs.pendingResults()

    def numberOfPendingResults(self, tag : str =None) -> int:
        '''Return the number of results pending in the tagged dataset.
        
        :params tag: (optional) the result set tag (defaults to the current set)
        :returns: the number of results'''
        if tag is None:
            rs = self._current
        else:
            rs = self._resultSets[tag]
        return rs.numberOfPendingResults()

    def pendingResultParameters(self, jobid : str) -> Dict[str, Any]:
        '''Return a dict of paramneters corresponding to the given pending result.

        :param jobid: the job id
        :returns: a dict of parameter values'''
        rs = self._pending[jobid]
        return rs.pendingResultParameters(jobid)


    # ---------- Managing pending results in all result sets ----------

    def allPendingResults(self) -> Set[str]:
        '''Return the identifiers for all pending results in all result sets.

        :returns: a set of job identifiers'''
        return set(self._pending.keys())

    def numberOfAllPendingResults(self) -> int:
        '''Return the number of results pending in all result sets.

        :returns: the total number of pending results'''
        return len(self._pending) 


    # --------- Managing results ----------

    def addResult(self, result : ResultsDict, tag : str =None):
        '''Add a single result. Client code should use :meth:`addResults`
        in preference to this method and work solely with the current result set.

        :param tag: (optional) the result set to add to (defaults to the current result set)
        :param result: the results dict'''
        if tag is None:
            rs = self._current
        else:
            rs = self._resultSets[tag]
        rs.addSingleResult(result)

    def addResults(self, results : Any):
        """Add one or more results dicts to the current result set. Each should
        be a :term:`results dict` as returned from
        an instance of :class:`Experiment`, that contains metadata,
        parameters, and result.

        The results may include one or more nested results dicts, for example as
        returned by :class:`RepeatedExperiment`, whose results are a list of results
        at the same point in the parameter space. In this case the embedded
        results will themselves be unpacked and added.

        One may also add a list of results dicts, in which case they will
        be added individually.

        :param result: a results dict or collection of them
        """

        # deal with the different ways of presenting results to be added
        if isinstance(ResultSet, list):
            # a list, recursively add all elements
            for res in results:
                self.addResult(res)
        else:
            if isinstance(results, dict):
                if isinstance(results[Experiment.RESULTS], list):
                    # a result with embedded results, unwrap and and add them
                    for res in results[Experiment.RESULTS]:
                        self.addResult(res)
                else:
                    # a single results dict with a single set of experimental results
                    self.addResult(results)

            else:
                raise Exception("Can't deal with results like this: {r}".format(r = results)) 
    
    def dataframe(self, tag : str =None, only_successful : bool =True) -> DataFrame:
        """Return results as a ``pandas.DataFrame``. If no tag is provided,
        use the current result set. 

        If the only_successful flag is set (the default), then the DataFrame will
        only include results that completed without an exception; if it is set to
        False, the DataFrame will include all results and also the exception details.

        If you are only interested in results corresponding to some sets of parameters
        you can pre-filter the dataframe using :meth:`dataframeFor`. 

        :params tag: (optional) the tag of the result set (defaults to the currently select result set)
        :param only_successful: include only successful experiments (defaults to True)
        :returns: the parameters, results, and metadata in a DataFrame"""
        if tag is None:
            rs = self._current
        else:
            rs = self._resultSets[tag]
        df = rs.dataframe()
        if len(df) > 0 and only_successful:
            # filter out only the successful runs (if there are any to start with)
            df = df[df[Experiment.STATUS] == True]
        return df

    def dataframeFor(self, params : Dict[str, Any], tag : str =None, only_successful : bool =True) -> DataFrame:
        """Return results for the goven parameter values as a ``pandas.DataFrame``.
        If no tag is provided, the current result set is queried. 
        If the only_successful flag is set (the default), then the DataFrame will
        only include results that completed without an exception; if it is set to
        False, the DataFrame will include all results and also the exception details.

        :param params: the experimental parameters
        :params tag: (optional) the tag of the result set (defaults to the currently select result set)
        :param only_successful: include only successful experiments (defaults to True)
        :returns: the parameters, results, and metadata in a DataFrame"""
        if tag is None:
            rs = self._current
        else:
            rs = self._resultSets[tag]
        df = rs.dataframeFor(params)
        if len(df) > 0 and only_successful:
            # filter out only the successful runs (if there are any to start with)
            df = df[df[Experiment.STATUS] == True]
        return df

    def results(self, tag : str =None) -> List[ResultsDict]:
        """Return results as a list of results dicts. If no tag is provided,
        use the current result set. This is a lot slower and more memory-hungry
        than using :meth:`dataframe` (which is therefore to be preferred),
        but may be useful for small sets of results that need a more Pythonic
        interface than that provided by DataFrames. You can pre-filter the
        results dicts to those matching only some parameters combinations
        using :meth:`resultsFor`.

        :params tag: (optional) the tag of the result set (defaults to the currently select result set)
        :returns: the results dicts"""
        if tag is None:
            rs = self._current
        else:
            rs = self._resultSets[tag]
        return rs.results()

    def resultsFor(self, params, tag : str =None) -> List[ResultsDict]:
        """Return results for the given parameter values a list of results dicts. If no tag is provided,
        use the current result set. This is a lot slower and more memory-hungry
        than using :meth:`dataframeFor` (which is therefore to be preferred),
        but may be useful for small sets of results that need a more Pythonic
        interface than that provided by DataFrames.

        :param params: the experimental parameters
        :returns: results dicts"""
        if tag is None:
            rs = self._current
        else:
            rs = self._resultSets[tag]
        return rs.resultsFor(params)

    def numberOfResults(self, tag : str =None) -> int:
        '''Return the number of results in the tagged dataset.
        
        :params tag: (optional) the result set tag (defaults to the current set)
        :returns: the number of results'''
        if tag is None:
            rs = self._current
        else:
            rs = self._resultSets[tag]
        return rs.numberOfResults()


    # ---------- Context manager protocol ----------

    @contextmanager
    def open(self):
        '''Open and close the notebook using a ``with`` block. For persistent
        notebooks this will cause the notebook to be committed to persistent
        storage in a robust manner.'''
        try:
            # nothing to do, as the operations all open as required
            yield self
        finally:
            # commit any changes and close the file
            self.commit()


