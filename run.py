import argparse
import importlib


def get_score(filename) -> int:
    score = 0
    return score


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Usage: python run.py <input filename> <algorithm filename>")
    parser.add_argument('input_file', type=str, help='Input filename')
    parser.add_argument('alg_file', type=str,
                        help='Filename of the algorithm; the algorithm needs to have run(filename) function'
                             'which returns name of the output file')
    args = parser.parse_args()
    alg = importlib.import_module(args.alg_file)
    output_file = alg.run(args.input_file)
    print(get_score(output_file))
