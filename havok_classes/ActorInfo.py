import struct


class ActorInfo(object):
    HashId: int
    SRTHash: int
    ShapeInfoStart: int
    ShapeInfoEnd: int

    def __init__(self, infile):
        self.HashId = struct.unpack('>I', infile.read(4))
        self.SRTHash = struct.unpack('>i', infile.read(4))
        self.ShapeInfoStart = struct.unpack('>i', infile.read(4))
        self.ShapeInfoEnd = struct.unpack('>i', infile.read(4))
