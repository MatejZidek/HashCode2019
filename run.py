import argparse
import importlib


def get_slide(photos, photos_line):
    photos_ids = [int(i) for i in photos_line.split()]
    slide = photos[photos_ids[0]]
    if len(photos_ids) == 2:
        slide = slide.join_v_photos(photos[photos_ids[1]])
    return slide


def get_score(photos, filename) -> int:
    score = 0
    with open(filename) as f:
        try:
            slide_count = f.readline()
            second_slide = get_slide(photos, f.readline())
            for i in range(2, slide_count):
                first_slide = second_slide
                second_slide = get_slide(photos, f.readline())
                score += first_slide.score(second_slide)
        except StopIteration:
            # Only one slide
            pass
    return score


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Usage: python run.py <input filename> <algorithm filename>")
    parser.add_argument('input_file', type=str, help='Input filename')
    parser.add_argument('alg_file', type=str, help='Filename of the algorithm without ".py"')
    args = parser.parse_args()
    alg = importlib.import_module(args.alg_file)
    photos, output_file = alg.run(args.input_file)
    print(get_score(photos, output_file))
