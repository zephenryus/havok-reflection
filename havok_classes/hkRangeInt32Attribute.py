import struct


class hkRangeInt32Attribute(object):
    absmin: int
    absmax: int
    softmin: int
    softmax: int

    def __init__(self, infile):
        self.absmin = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.absmax = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.softmin = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.softmax = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} absmin={absmin}, absmax={absmax}, softmin={softmin}, softmax={softmax}>".format(**{
            "class_name": self.__class__.__name__,
            "absmin": self.absmin,
            "absmax": self.absmax,
            "softmin": self.softmin,
            "softmax": self.softmax,
        })
