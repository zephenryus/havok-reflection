class hkDescriptionAttribute(object):
    string: str

    def __init__(self, infile):
        self.string = str(infile)  # TYPE_CSTRING:TYPE_VOID

    def __repr__(self):
        return "<{class_name} string=\"{string}\">".format(**{
            "class_name": self.__class__.__name__,
            "string": self.string,
        })
