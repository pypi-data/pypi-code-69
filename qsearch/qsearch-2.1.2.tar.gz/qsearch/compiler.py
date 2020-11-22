"""
This module defines the Compiler class, which is a framework for classes that take a unitary and return a circuit implementing that unitary.

The default implementation SearchCompiler is also defined here.  SearchCompiler compiles the desired unitary using an A* search strategy, as described in the paper Towards Optimal Topology Aware Quantum Circuit Synthesis.
"""
from functools import partial
from timeit import default_timer as timer
import heapq

from .gates import *

from . import solvers as scsolver
from .options import Options
from .defaults import standard_defaults, standard_smart_defaults
from . import parallelizers, backends
from . import utils, heuristics, gates, logging, gatesets

class Compiler():
    """This class defines the pattern for compilers that convert a unitary matrix to a circuit that implements that matrix."""
    def __init__(self, options=Options()):
        self.options = options

    def compile(self, options):
        raise NotImplementedError("Subclasses of Compiler are expected to implement the compile method.")
        return (U, None)

class SearchCompiler(Compiler):
    """This Compiler uses an A* search strategy to synthesize a unitary, as described in the paper Towards Optimal Topology Aware Quantum Circuit Synthesis.

    Options:
        target (required) : The unitary matrix to be synthesized, in the form of a numpy ndarray with dtype="complex128".
        gateset : The Gateset used for synthesis.
        weight_limit : A limit on the maximum weight for circuits to be expanded for further searching.  See gatesets.py for more information.  The default is None for unlimited.
        heuristic : A heuristic used to order the search tree.  See heuristics.py for more information.
        solver : A Solver used for optimizing the parameters in parameterized circuits generated by the search tree.
        parallelizer : A Parallelizer used for solving multiple parameterized circuits in parallel.
        beams : The number of nodes to pop from the search tree at a time.  The default value of -1 will create enough branches to maximize utilization of your CPU.
        error_func : The function that the Solver will attempt to minimize.
        eval_func : The function used by the heuristic in order to guide the search tree.  By default this is equal to error_func.
        error_jac : A function that returns a tuple of the value that error_func would generate and the jacobian of error_func
        error_residuals : A function that returns an array of real-valued residuals to be used by a least-squares-based Solver.
        error_residuals_jac : A function that returns the jacobian of error_residuals (note that it does NOT return a tuple of the residuals and the jacobian).
        timeout : An uper limit on the amount of time the compiler will spend trying to synthesize a circuit.  The default is float('inf'), for unlimited.
        checkpoint : The compiler will use this Checkpoint to save intermediate state, and will resume from this Checkpoint if there was an existing state.
        logger : A qsearch.logging.Logger that will be used for logging the synthesis process.

    """
    def __init__(self, options=Options()):
        """
        Args:
            options: See class level documentation for the options SearchCompiler uses
        """
        self.options = options
        self.options.set_defaults(**standard_defaults)
        self.options.set_defaults(verbosity=1, logfile=None, stdout_enabled=True)
        self.options.set_smart_defaults(**standard_smart_defaults)

    def compile(self, options=Options()):
        """
        Args:
            options: See class level documentation for the options SearchCompiler uses
        """
        options = self.options.updated(options)
        options.make_required("target")

        if "unitary_preprocessor" in options:
            U = options.unitary_preprocessor(options.target)
        weight_limit = options.weight_limit
        checkpoint = options.checkpoint
        logger = options.logger

        starttime = timer() #NOTE because all of this setup gets included in the total time, stopping and restarting the project may lead to time durations that are not representative of the runtime under normal conditions.
        h = options.heuristic
        qudits = int(np.round(np.log(np.shape(U)[0])/np.log(options.gateset.d)))

        if options.gateset.d**qudits != np.shape(U)[0]:
            raise ValueError("The target matrix of size {} is not compatible with qudits of size {}.".format(np.shape(U)[0], self.options.gateset.d))

        I = gates.IdentityGate(d=options.gateset.d)

        initial_layer = options.gateset.initial_layer(qudits)
        branching_factor = options.gateset.branching_factor(qudits)
        if branching_factor <= 0:
            logger.logprint("This gateset has no branching factor so only an initial optimization will be run.")
            root = initial_layer
            result = options.solver.solve_for_unitary(options.backend.prepare_circuit(root, options), options)
            return (root, result[1])

        parallel = options.parallelizer(options)
        # TODO move these print statements somewhere like parallelizers possibly
        logger.logprint("There are {} processors available to Pool.".format(options.num_tasks))
        logger.logprint("The branching factor is {}.".format(branching_factor))
        beams = int(options.beams)
        if beams < 1 and branching_factor > 0:
            beams = int(options.num_tasks // branching_factor)
        if beams < 1:
            beams = 1
        if beams > 1:
            logger.logprint("The beam factor is {}.".format(beams))

        recovered_state = checkpoint.recover()
        queue = []
        best_weight = 0
        best_value = 0
        best_pair  = 0
        tiebreaker = 0
        rectime = 0
        if recovered_state == None:
            if isinstance(initial_layer, ProductGate):
                root = initial_layer
            else:
                root = ProductGate(initial_layer)
            root = ProductGate(initial_layer)
            result = options.solver.solve_for_unitary(options.backend.prepare_circuit(root, options), options)
            best_value = options.eval_func(U, result[0])
            best_pair = (root, result[1])
            logger.logprint("New best! {} at weight 0".format(best_value))
            if weight_limit == 0:
                return best_pair

            queue = [(h(*best_pair, 0, options), 0, best_value, -1, result[1], root)]
            #         heuristic      weight  distance tiebreaker parameters structure
            #             0            1      2         3         4        5
            checkpoint.save((options, queue, best_weight, best_value, best_pair, tiebreaker, timer()-starttime))
        else:
            options, queue, best_weight, best_value, best_pair, tiebreaker, rectime = recovered_state
            if options.load_error:
                logger.logprint("Failed to recover state from checkpoint.  Resolve the issue or delete the checkpoint to finish the compilation.", 0)
                raise options.load_error
            logger.logprint("Recovered state with best result {} at weight {}".format(best_value, best_weight))

        options.generate_cache() # Cache the results of smart_default settings, such as the default solver, before entering the main loop where the options will get pickled and the smart_default functions called many times because later caching won't persist cause of pickeling and multiple processes.

        while len(queue) > 0:
            if timer() - starttime > options.timeout:
                break
            if best_value < options.threshold:
                queue = []
                break
            popped = []
            for _ in range(0, beams):
                if len(queue) == 0:
                    break
                tup = heapq.heappop(queue)
                popped.append(tup)
                logger.logprint("Popped a node with score: {} at weight: {}".format((tup[2]), tup[1]), verbosity=2)

            then = timer()
            new_steps = [(successor[0], current_tup[1], successor[1]) for current_tup in popped for successor in options.gateset.successors(current_tup[5])]
            for step, result, current_weight, weight in parallel.solve_circuits_parallel(new_steps):
                current_value = options.eval_func(U, result[0])
                new_weight = current_weight + weight
                if (current_value < best_value and (best_value >= options.threshold or new_weight <= best_weight)) or (current_value < options.threshold and new_weight < best_weight):
                    best_value = current_value
                    best_pair = (step, result[1])
                    best_weight = new_weight
                    logger.logprint("New best! score: {} at weight: {}".format(best_value, new_weight))
                if weight_limit is None or new_weight < weight_limit:
                    heapq.heappush(queue, (h(step, result[1], new_weight, options), new_weight, current_value, tiebreaker, result[1], step))
                    tiebreaker+=1
            logger.logprint("Layer completed after {} seconds".format(timer() - then), verbosity=2)
            checkpoint.save((options, queue, best_weight, best_value, best_pair, tiebreaker, rectime+(timer()-starttime)))


        logger.logprint("Finished compilation at weight {} with score {} after {} seconds.".format(best_weight, best_value, rectime+(timer()-starttime)))
        parallel.done()
        return {'structure': best_pair[0], 'parameters': best_pair[1]}

