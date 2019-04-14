from tspsolver.path import Path, RandomPath

from pytest import approx


def testPathGetVertices():
    V = [(1, 2), (2, 3)]
    p = Path(V)
    assert p.get_vertices() == V


def testPathDistance():
    assert Path._distance((1, 1), (1, 2)) == 1
    assert Path._distance((1, 2), (1, 1)) == 1
    assert Path._distance((1, 1), (2, 1)) == 1
    assert Path._distance((2, 1), (1, 1)) == 1
    assert Path._distance((1, 1), (2, 2)) == approx(1.41, 0.01)


def testPathPermute():
    p = Path([(0, 0), (1, 1), (2, 2), (3, 3)])
    p.permute([1, 3, 2, 0])
    assert p.get_vertices() == [(1, 1), (3, 3), (2, 2), (0, 0)]
    p.permute([3, 0, 2, 1])
    assert p.get_vertices() == [(0, 0), (1, 1), (2, 2), (3, 3)]


def testPathGetCycleLength_without_permutation():
    assert Path([]).get_cycle_length() == 0
    assert Path([(1, 1)]).get_cycle_length() == 0
    assert Path([(1, 1), (2, 1)]).get_cycle_length() == 2
    assert Path([(1, 1), (2, 1), (2, 2)]).get_cycle_length()\
        == approx(3.41, 0.01)
    assert Path([(1, 1), (2, 1), (2, 2), (1, 2)]).get_cycle_length() == 4
    assert Path([(1, 1), (2, 2), (2, 3), (1, 3)]).get_cycle_length()\
        == approx(5.41, 0.01)


def testPathGetCycleLength_with_permutation():
    assert Path([(1, 1)]).get_cycle_length([0]) == 0
    assert Path([(1, 1), (2, 1)]).get_cycle_length([1, 0]) == 2
    assert Path([(2, 1), (1, 1), (2, 2)]).get_cycle_length([1, 0, 2])\
        == approx(3.41, 0.01)
    assert Path([(2, 2), (1, 2), (1, 1), (2, 1)],
                ).get_cycle_length([2, 3, 0, 1]) == 4
    assert Path([(1, 1), (2, 2), (2, 3), (1, 3)],
                ).get_cycle_length([0, 1, 2, 3]) == approx(5.41, 0.01)


def testPathLoad(tmp_path):
    file_path = tmp_path / "test_dataset.tsv"
    file_path.write_text("1.0 0.0\n1.1 0.1\n3.0 3.1")
    p = Path()
    p.load(str(file_path))
    assert p.get_vertices() == [(1.0, 0.0), (1.1, 0.1), (3.0, 3.1)]


def testRandomPathInit():
    path = RandomPath(100, (1, 5))
    assert len(path._vertices) == 100
    for x, y in path._vertices:
        assert type(x) is float
        assert type(y) is float
        assert x <= 5
        assert x >= 1
        assert y <= 5
        assert y >= 1
