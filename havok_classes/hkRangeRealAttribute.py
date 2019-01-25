import struct


class hkRangeRealAttribute(object):
    absmin: float
    absmax: float
    softmin: float
    softmax: float

    def __init__(self, infile):
        self.absmin = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.absmax = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.softmin = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.softmax = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} absmin={absmin}, absmax={absmax}, softmin={softmin}, softmax={softmax}>".format(**{
            "class_name": self.__class__.__name__,
            "absmin": self.absmin,
            "absmax": self.absmax,
            "softmin": self.softmin,
            "softmax": self.softmax,
        })
