from tspsolver.path import Path

from pytest import approx


def test_get_vertices():
    V = [(1, 2), (2, 3)]
    p = Path(V)
    assert p.get_vertices() == V


def test_distance():
    assert Path._distance((1, 1), (1, 2)) == 1
    assert Path._distance((1, 2), (1, 1)) == 1
    assert Path._distance((1, 1), (2, 1)) == 1
    assert Path._distance((2, 1), (1, 1)) == 1
    assert Path._distance((1, 1), (2, 2)) == approx(1.41, 0.01)


def test_get_cycle_length():
    assert Path([]).get_cycle_length() == 0
    assert Path([(1, 1)]).get_cycle_length() == 0
    assert Path([(1, 1), (2, 1)]).get_cycle_length() == 2
    assert Path([(1, 1), (2, 1), (2, 2)]).get_cycle_length()\
        == approx(3.41, 0.01)
    assert Path([(1, 1), (2, 1), (2, 2), (1, 2)]).get_cycle_length() == 4
    assert Path([(1, 1), (2, 2), (2, 3), (1, 3)]).get_cycle_length()\
        == approx(5.41, 0.01)


def test_load(tmp_path):
    file_path = tmp_path / "test_dataset.tsv"
    file_path.write_text("1.0 0.0\n1.1 0.1\n3.0 3.1")
    p = Path()
    p.load(str(file_path))
    assert p.get_vertices() == [(1.0, 0.0), (1.1, 0.1), (3.0, 3.1)]
