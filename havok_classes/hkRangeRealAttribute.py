import struct


class hkRangeRealAttribute(object):
    absmin: float
    absmax: float
    softmin: float
    softmax: float

    def __init__(self, infile):
        self.absmin = struct.unpack('>f', infile.read(4))
        self.absmax = struct.unpack('>f', infile.read(4))
        self.softmin = struct.unpack('>f', infile.read(4))
        self.softmax = struct.unpack('>f', infile.read(4))
