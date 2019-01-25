import struct


class hkSimplePropertyValue(object):
    data: int

    def __init__(self, infile):
        self.data = struct.unpack('>Q', infile.read(8))
