import random

from file_handler import File


def get_tag_dict(photos_dict) -> dict:
    tag_dict = dict()
    for photo_id, photo in photos_dict.items():
        for tag in photo.tags:
            if tag in tag_dict:
                tag_dict[tag].append(photo_id)
            else:
                tag_dict[tag] = [photo_id, ]
    return tag_dict


def find_next(photo, photos, photos_tags):
    for tag in photo.tags:
        if tag in photos_tags and len(photos_tags[tag]) == 0:
            photos_tags.pop(tag)
        elif tag in photos_tags:
            return photos_tags[tag].pop(0)
    return random.choice(list(photos.keys()))


def process(photos) -> list:
    """
    :param photos: List of photos object
    :return: slideshow: list of tuples in the correct format
    """
    slides = []

    v_photos = {i: photos[i] for i in range(len(photos)) if photos[i].orientation == 'V'}
    h_photos = {i: photos[i] for i in range(len(photos)) if photos[i].orientation == 'H'}

    if len(v_photos) % 2 == 1:
        v_photos.popitem()
    if len(h_photos) == 0:
        return slides
    v_photos_tags = get_tag_dict(v_photos)
    h_photos_tags = get_tag_dict(h_photos)

    # print(list(h_photos.keys())[:50])
    # print(h_photos_tags)
    slides.append(h_photos.popitem()[0])
    while len(h_photos) > 0:
        next_photo = find_next(photos[slides[-1]], h_photos, h_photos_tags)
        slides.append(next_photo)
        try:
            h_photos.pop(next_photo)
        except:
            pass
    while len(v_photos):
        slides.append((v_photos.popitem()[0], v_photos.popitem()[0]))
    return slides


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
