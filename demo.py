from tspsolver.path import Path
from tspsolver.pathplotter import PathPlotter
from tspsolver.randomsolver import RandomSolver
from tspsolver.evolutionarysolver import EvolutionarySolver


def main():
    path = Path()
    path.load('./data/dataset.tsv')
    plotter = PathPlotter()
    # plotter.plot(path)
    print('original length:', path.get_cycle_length())
    solver = RandomSolver(path, 100)
    path = solver.solve()
    print('randomly solved length:', path.get_cycle_length())
    # plotter.plot(path)
    solver = EvolutionarySolver(path, verbose=True)
    path = solver.solve()
    print('evolutionary solved length:', path.get_cycle_length())
    plotter.plot(path)
    plotter.show()
    return 0


if __name__ == "__main__":
    main()
