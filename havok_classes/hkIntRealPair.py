import struct


class hkIntRealPair(object):
    key: int
    value: float

    def __init__(self, infile):
        self.key = struct.unpack('>i', infile.read(4))
        self.value = struct.unpack('>f', infile.read(4))
