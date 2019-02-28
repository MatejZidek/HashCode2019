class File:
    def __init__(self):
        # init fields
        pass

    # getters & setters

    def __str__(self):
        return ""

    def read_input(self, filename):
        with open(filename) as f:
            # process special lines

            # process the rest
            for line in f:
                pass

    def write_output(self, filename):
        with open(filename, "w") as f:
            pass
