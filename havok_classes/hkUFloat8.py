import struct


class hkUFloat8(object):
    value: int

    def __init__(self, infile):
        self.value = struct.unpack('>B', infile.read(1))
