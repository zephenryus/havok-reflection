import struct


class hkaiAdaptiveRanger(object):
    curRange: float

    def __init__(self, infile):
        self.curRange = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} curRange={curRange}>".format(**{
            "class_name": self.__class__.__name__,
            "curRange": self.curRange,
        })
