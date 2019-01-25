import struct


class hkPackedVector3(object):
    values: int

    def __init__(self, infile):
        self.values = struct.unpack('>h', infile.read(2))
