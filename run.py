import argparse
import importlib

from photo import Photo


def get_slide(photos_line):
    photos_ids = [int(i) for i in photos_line.split()]
    slide = photos[photos_ids[0]]
    if len(photos_ids) == 2:
        slide = slide.join_v_photos(photos[photos_ids[1]])
    return slide


def get_score(filename) -> int:
    score = 0
    with open(filename) as f:
        slide_count = int(f.readline())
        if slide_count == 0:
            return score
        second_slide = get_slide(f.readline())
        for i in range(2, slide_count):
            first_slide = second_slide
            second_slide = get_slide(f.readline())
            score += first_slide.score(second_slide)
    return score


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Usage: python run.py <input filename> <algorithm filename>")
    parser.add_argument('input_file', type=str, help='Input filename')
    parser.add_argument('alg_file', type=str, help='Filename of the algorithm without ".py"')
    args = parser.parse_args()
    alg = importlib.import_module(args.alg_file)
    photos, output_file = alg.run(args.input_file)
    print(get_score(output_file))
