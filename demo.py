from tspsolver.path import Path
from tspsolver.pathplotter import PathPlotter
from tspsolver.randomsolver import RandomSolver


def main():
    path = Path()
    path.load('./data/dataset.tsv')
    plotter = PathPlotter()
    plotter.plot(path)
    print('original length:', path.get_cycle_length())
    solver = RandomSolver(path, 100000)
    path = solver.solve()
    print('randomly solved length:', path.get_cycle_length())
    plotter.plot(path)
    plotter.show()
    return 0


if __name__ == "__main__":
    main()
