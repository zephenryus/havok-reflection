from .hkReferencedObject import hkReferencedObject


class hkLocalFrameGroup(hkReferencedObject):
    name: str

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\">".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
        })
