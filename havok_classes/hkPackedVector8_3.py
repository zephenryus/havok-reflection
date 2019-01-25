import struct


class hkPackedVector8_3(object):
    values: int

    def __init__(self, infile):
        self.values = struct.unpack('>b', infile.read(1))
