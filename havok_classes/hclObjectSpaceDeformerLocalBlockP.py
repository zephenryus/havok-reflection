import struct


class hclObjectSpaceDeformerLocalBlockP(object):
    localPosition: int

    def __init__(self, infile):
        self.localPosition = struct.unpack('>h', infile.read(2))
