import argparse
import sys

from tspsolver.path import Path, RandomPath
from tspsolver.pathplotter import PathPlotter
from tspsolver.evolutionarysolver import EvolutionarySolver


def main():
    parser = argparse.ArgumentParser(
        description='Travelling Salesman Problem solver using (Mu+Lambda)\
                     Evolutionary Algorithm')
    parser.add_argument('--file', '-f',
                        help='input file path',
                        type=argparse.FileType('r'))
    parser.add_argument('--vertices', '-vert',
                        help='number of vertices to be genarated \
                        if no input file is used',
                        type=int, default=78)
    parser.add_argument('--fast',
                        help='use smaller population to shorten computation',
                        action='store_true')
    parser.add_argument('--generations', '-gen',
                        help='number of generations',
                        type=int, default=500)
    parser.add_argument('--verbose', '-v',
                        help='increase output verbosity',
                        action='store_true')
    args = parser.parse_args()

    if args.file is not None:
        path = Path()
        print("Loading vertices from file:", args.file.name, '...')
        path.load(args.file)
    else:
        print("Generating random vertices...")
        path = RandomPath(args.vertices)
    print('Number of vertices:', path.get_number_of_vertices())

    print('Length of input path:', path.get_cycle_length())
    if args.fast:
        print('Using smaller population for faster computation.')
        solver = EvolutionarySolver(path,
                                    population_size=100,
                                    mu=100, lambda_=300,
                                    ngen=args.generations,
                                    verbose=args.verbose)
    else:
        solver = EvolutionarySolver(path,
                                    ngen=args.generations,
                                    verbose=args.verbose)
    print('Solving TSP...', end='\n' if args.verbose else ' ')
    sys.stdout.flush()
    path = solver.solve()
    print('done.')
    print('Evolutionary solved length:', path.get_cycle_length())
    print('Plotting solution...')
    plotter = PathPlotter()
    plotter.plot(path)
    plotter.show()
    print('Bye.')
    return 0


if __name__ == "__main__":
    main()
