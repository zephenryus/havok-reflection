import struct


class hclObjectSpaceDeformerLocalBlockPNTB(object):
    localPosition: int
    localNormal: int
    localTangent: int
    localBiTangent: int

    def __init__(self, infile):
        self.localPosition = struct.unpack('>h', infile.read(2))
        self.localNormal = struct.unpack('>h', infile.read(2))
        self.localTangent = struct.unpack('>h', infile.read(2))
        self.localBiTangent = struct.unpack('>h', infile.read(2))
