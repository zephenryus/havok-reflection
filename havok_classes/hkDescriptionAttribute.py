class hkDescriptionAttribute(object):
    string: str

    def __init__(self, infile):
        self.string = str(infile)  # TYPE_CSTRING
