from tspsolver.evolutionarysolver import EvolutionarySolver

from tspsolver.path import Path


def testSolve():
    original_vertices = [(1, 1), (1, 2), (0, 0), (0, 3)]
    path = Path(original_vertices)
    solver = EvolutionarySolver(path, population_size=10, ngen=100)
    solution = solver.solve()
    solution_vertices = solution.get_vertices()
    assert len(solution_vertices) == len(original_vertices)
    assert set(solution_vertices) == set(original_vertices)
