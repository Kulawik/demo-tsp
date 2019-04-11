from tspsolver.path import Path
from tspsolver.pathplotter import PathPlotter


def main():
    path = Path()
    path.load('../data/dataset.tsv')
    plotter = PathPlotter()
    plotter.plot(path)
    plotter.show()
    return 0

if __name__ == "__main__":
    main()
