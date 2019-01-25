import struct


class hclObjectSpaceDeformerLocalBlockPN(object):
    localPosition: int
    localNormal: int

    def __init__(self, infile):
        self.localPosition = struct.unpack('>h', infile.read(2))
        self.localNormal = struct.unpack('>h', infile.read(2))
