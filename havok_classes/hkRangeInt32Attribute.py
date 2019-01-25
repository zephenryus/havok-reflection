import struct


class hkRangeInt32Attribute(object):
    absmin: int
    absmax: int
    softmin: int
    softmax: int

    def __init__(self, infile):
        self.absmin = struct.unpack('>i', infile.read(4))
        self.absmax = struct.unpack('>i', infile.read(4))
        self.softmin = struct.unpack('>i', infile.read(4))
        self.softmax = struct.unpack('>i', infile.read(4))
