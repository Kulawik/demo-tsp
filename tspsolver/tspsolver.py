from abc import ABC, abstractmethod

from tspsolver.path import Path


class TSPSolver(ABC):
    """ Abstract base class of Travelling Salesman Problem Solver
    """

    def __init__(self, path: Path):
        """Inits the TSPSolver with path.

        Args:
            paths: Path representing any path in a graph of points on a plane.
        """
        self.path = path

    @abstractmethod
    def solve(self) -> Path:
        """Abstract method solving the TSP.

        Returns:
            Result path.
        """
        return self.path
