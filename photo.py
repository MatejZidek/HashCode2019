class Photo:
    # ori is orientation, tags is a list of strings
    def __init__(self, ori, tags):
        self.orientation = ori
        self.tags = set(map(str.strip, tags))

    def __str__(self):
        return self.orientation + " " + " ".join(self.tags)

    def overlap(self, otherPhoto):
        return otherPhoto.tags & self.tags

    def join_v_photos(self, other_h_photo):
        joined_photo = Photo()
        joined_photo.orientation = 'V'
        joined_photo.tags = self.tags.union(other_h_photo.tags)
        return joined_photo

    def score(self, next_photo):
        only_self = self.tags - next_photo.tags
        only_next = next_photo.tags - self.tags
        both = self.tags.intersection(next_photo.tags)
        return min(len(only_self), len(only_next), len(both))
