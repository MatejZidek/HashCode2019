from file_handler import File
tagDict = dict()

def match(photo, photoUsed):
    for tag in photo.tags:
        for photoID in tagDict[tag]:
            if not photoUsed[photoID]:
                return photoID
    return -1

def process(photos) -> list:
    """
    :param photos: List of photos object
    :return: slideshow: list of tuples in the correct format
    """
    
    for i in range(len(photos)):
        for tag in photos[i].tags:
            if tag in tagDict:
                tagDict[tag].append(i)
            else:
                tagDict[tag] = [i,]
    photoUsed = [False] * len(photos)
    slides = []
    nextPhoto = 0
    while (nextPhoto != -1):
        slides.append(nextPhoto)
        photoUsed[nextPhoto] = True
        nextPhoto = match(photos[nextPhoto], photoUsed)
                
    return slides

def run(filename) -> str:
    """
    :param filename: input filename
    :return: output filename
    """
    f = File()
    photos = f.read_input(filename)
    slideshow = process(photos)
    out_filename = "{}-out.txt".format(filename.split(".")[0])
    f.write_output(out_filename, slideshow)
    return out_filename




    #Put all photos into hash table on tags
    # Key is tag, Element is list of indexes

    #Find tag with most photos
    #Join all of those as slides
    #Return