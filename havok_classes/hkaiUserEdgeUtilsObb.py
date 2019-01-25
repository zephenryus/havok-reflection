import struct


class hkaiUserEdgeUtilsObb(object):
    transform: any
    halfExtents: vector4

    def __init__(self, infile):
        self.transform = any(infile)  # TYPE_TRANSFORM:TYPE_VOID
        self.halfExtents = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transform={transform}, halfExtents={halfExtents}>".format(**{
            "class_name": self.__class__.__name__,
            "transform": self.transform,
            "halfExtents": self.halfExtents,
        })
