from typing import List, Tuple, TextIO
from math import sqrt
import csv
import random

Vertex = Tuple[float, float]
Vertices = List[Vertex]


class Path:
    """Path on a plane

    Path is representing a path in a graph of points on a plane.
    """

    def __init__(self, vertices: Vertices = []):
        """Inits Path with vertices

        Args:
            vertices: list of vertices represented by tuples (float, float)
        """
        self._vertices = vertices

    def load(self, input_file: TextIO):
        """Loads vertices from file

        Args:
            input_file: input_file
        """
        reader = csv.reader(input_file, delimiter=' ')
        self._vertices = [(float(row[0]), float(row[1])) for row in reader]

    def get_vertices(self) -> Vertices:
        """Returns vertices list"""
        return self._vertices

    def get_number_of_vertices(self) -> int:
        """Return number of vertices"""
        return len(self._vertices)

    def permute(self, indices: List[int]):
        """Permutes the vertices

        Args:
            indices: list of indices representing permutation,
                     validity of indices is not checked
        """
        self._vertices = [self._vertices[i] for i in indices]

    def get_cycle_length(self, indices: List[int] = None) -> float:
        """Returns cycle length

        Calculates length of cycle created by connecting first and last vertex
        from the vertices. If indices are provided, the length is calculated
        for the given permutation of vertices.

        Args:
            indices: list of indices representing permutation.
                     validity of indices is not checked
        """
        if len(self._vertices) < 2:
            return 0
        if indices is None:
            indices = range(len(self._vertices))
        return sum([Path._distance(self._vertices[indices[i]],
                                   self._vertices[indices[i + 1]])
                    for i in range(len(indices) - 1)])\
            + Path._distance(self._vertices[indices[-1]],
                             self._vertices[indices[0]])

    def _distance(v0: Vertex, v1: Vertex) -> float:
        """Calculates euclidean distance between points

        Args:
            v0: Vertex representing first point.
            v1: Vertex representing second point.

        Returns:
            Euclidean distance between points.
        """
        return sqrt((v1[0] - v0[0])**2 + (v1[1] - v0[1])**2)


class RandomPath(Path):
    """Random path class"""
    def __init__(self, number_of_vertices: int,
                 limits: Tuple[float, float] = (0, 1)):
        """Inits RandomPath with random vertices

        Args:
            number_of_vertices: specifies number of vertices
                                in the generated path.
            limits: tuple (min, max) specifying range of each of coordinates,
                    defaults to (0, 1).
        """
        def generator():
            return random.uniform(*limits)
        self._vertices = [(generator(), generator())
                          for _ in range(number_of_vertices)]
