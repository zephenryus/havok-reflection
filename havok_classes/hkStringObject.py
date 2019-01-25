from .hkReferencedObject import hkReferencedObject


class hkStringObject(hkReferencedObject):
    string: str

    def __init__(self, infile):
        self.string = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} string=\"{string}\">".format(**{
            "class_name": self.__class__.__name__,
            "string": self.string,
        })
