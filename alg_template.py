from file_handler import File


def process(file) -> list:
    """
    :param file: File object
    :return: slideshow: list of tuples in the correct format
    """
    return []

def run(filename) -> str:
    """
    :param filename: input filename
    :return: output filename
    """
    f = File()
    f.read_input()
    slideshow = process(f)
    out_filename = "{}-out.txt".format(filename.split(".")[0])
    f.write_output(out_filename, slideshow)
    return out_filename

