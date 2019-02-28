from photo import Photo

class File:
    def __init__(self):
        pass

    # getters & setters

    def __str__(self):
        return " ".join([str(photo) for photo in self.photos])

    def read_input(self, filename):
        photos = list()
        with open(filename) as f:
            # process special lines
            numPhotos = f.readline()
            for i in range(int(numPhotos)):
                photoDetails = f.readline()
                details = photoDetails.split(" ")
                orientation = details[0]
                numTags = details[1]
                tags = details[2:]
                photos.append(Photo(orientation, tags))
        return photos


    def write_output(self, filename):
        with open(filename, "w") as f:
            pass
