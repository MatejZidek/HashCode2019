from file_handler import File


def process(photos) -> list:
    """
    :param photos: List of photos object
    :return: slideshow: list of tuples in the correct format
    """
    v_photos = {i: photos[i] for i in range(len(photos)) if photos[i].orientation == 'V'}
    h_photos = {i: photos[i] for i in range(len(photos)) if photos[i].orientation == 'H'}

    return []


def run(filename) -> tuple:
    """
    :param filename: input filename
    :return: photos list, output filename
    """
    f = File()
    photos = f.read_input(filename)
    slideshow = process(photos)
    out_filename = "{}-out.txt".format(filename.split(".")[0])
    f.write_output(out_filename, slideshow)
    return photos, out_filename
