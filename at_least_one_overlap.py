from file_handler import File


def process(photos) -> list:
    """
    :param photos: List of photos object
    :return: slideshow: list of tuples in the correct format
    """
    tag_dict = dict()
    for i in range(len(photos)):
        for tag in photos[i].tags:
            if tag in tag_dict:
                tag_dict[tag].append(i)
            else:
                tag_dict[tag] = [i, ]
    print(tag_dict)
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

