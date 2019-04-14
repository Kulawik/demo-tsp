from tspsolver.tspsolver import TSPSolver
from tspsolver.path import Path

from deap import creator, base, tools, algorithms
from random import sample
import numpy


class EvolutionarySolver(TSPSolver):
    """TSP solver using evolutionary algorithm.
    """

    def __init__(self, path: Path,
                 population_size: int = 200,
                 mu: int = 200,
                 lambda_: int = 600,
                 cxpb: float = 0.7,
                 mutpb: float = 0.2,
                 ngen: int = 500,
                 tourn_size: int = 4,
                 indpb: float = 0.05,
                 verbose: bool = False):
        """Inits EvolutionarySolver with path and population size.

        Args:
            path: Path representing any path in a graph of points on a plane.
            population_size: population size.
            cxpb: crossover probability.
            mutpb: mutation probability.
            ngen: number of generations.
            tourn_size: tournament size (selection parameter).
            indpb: independent probability for each vertice in a path
                   to be exchanged to another position.
            verbose: weather or not to print statistics.
        """
        super(EvolutionarySolver, self).__init__(path)
        self._population_size = population_size
        self._mu = mu
        self._lambda = lambda_
        self._cxpb = cxpb
        self._mutpb = mutpb
        self._ngen = ngen
        self._tourn_size = tourn_size
        self._indpb = indpb
        self._verbose = verbose
        self._init_deap()

    def solve(self) -> Path:
        """Solves TSP with simple evolutionary algorithm.

        Returns:
            Result path.
        """
        population = self._toolbox.population(n=self._population_size)
        hall_of_fame = tools.HallOfFame(maxsize=1)
        population, self._log = algorithms.eaMuPlusLambda(
            population, self._toolbox, mu=self._mu, lambda_=self._lambda,
            cxpb=self._cxpb, mutpb=self._mutpb, ngen=self._ngen,
            stats=self._stats, halloffame=hall_of_fame, verbose=self._verbose)
        indices = hall_of_fame[0]
        self.path.permute(indices)
        return self.path

    def get_log(self) -> tools.Logbook:
        """Gets last run logbook.

        Returns:
            deap.tools.Logbook with evolution process statistics.
        """
        return self._log

    def _init_deap(self):
        """Initializes deap framework."""
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)
        self._toolbox = base.Toolbox()
        vertices_len = len(self.path.get_vertices())
        self._toolbox.register("indices", sample, range(vertices_len),
                               vertices_len)
        self._toolbox.register("individual", tools.initIterate,
                               creator.Individual, self._toolbox.indices)
        self._toolbox.register("population", tools.initRepeat, list,
                               self._toolbox.individual)

        def evaluate(individual):
            return (self.path.get_cycle_length(individual),)
        self._toolbox.register("evaluate", evaluate)
        self._toolbox.register("mate", tools.cxOrdered)
        self._toolbox.register("mutate", tools.mutShuffleIndexes,
                               indpb=self._indpb)
        self._toolbox.register("select", tools.selTournament,
                               tournsize=self._tourn_size)
        self._stats = tools.Statistics(key=lambda ind: ind.fitness.values)
        self._stats.register("avg", numpy.mean)
        self._stats.register("std", numpy.std)
        self._stats.register("min", numpy.min)
        self._stats.register("max", numpy.max)
