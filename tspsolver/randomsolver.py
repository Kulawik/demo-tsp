from tspsolver.tspsolver import TSPSolver
from tspsolver.path import Path

from random import sample


class RandomSolver(TSPSolver):
    """Random solver of TSP

    Dummy approximate solver of TSP.
    Chooses best from population of random solutions.
    """

    def __init__(self, path: Path, population: int):
        """Inits RandomSolver with path and population size

        Args:
            paths: Path representing any path in a graph of points on a plane.
            population: integer random solutions population size.
        """
        super(RandomSolver, self).__init__(path)
        self.population = population

    def solve(self) -> Path:
        """Solves TSP with random approach

        Generates solution by choosing best path from population
        of random paths. The population size is given by population attribute.

        Returns:
            Result path.
        """
        vertices = self.path.get_vertices()
        vertices_len = len(vertices)
        return min([Path(sample(vertices, vertices_len))
                    for _ in range(self.population)],
                   key=lambda x: x.get_cycle_length())
