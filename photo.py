class Photo:
    #ori is orientation, tags is a list of strings
    def __init__(self, ori, tags):
        self.orientation = ori
        self.tags = set(map(str.strip, tags))

    def __str__(self):
        return self.orientation + " " + " ".join(self.tags)

    def overlap(otherPhoto):
        return otherPhoto.tags & self.tags