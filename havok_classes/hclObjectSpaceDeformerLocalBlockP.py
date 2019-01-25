import struct


class hclObjectSpaceDeformerLocalBlockP(object):
    localPosition: int

    def __init__(self, infile):
        self.localPosition = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} localPosition={localPosition}>".format(**{
            "class_name": self.__class__.__name__,
            "localPosition": self.localPosition,
        })
