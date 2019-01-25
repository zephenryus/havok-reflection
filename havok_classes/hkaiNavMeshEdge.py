import struct
from .common import any


class hkaiNavMeshEdge(object):
    a: int
    b: int
    oppositeEdge: int
    oppositeFace: int
    flags: any
    paddingByte: int
    userEdgeCost: int

    def __init__(self, infile):
        self.a = struct.unpack('>i', infile.read(4))
        self.b = struct.unpack('>i', infile.read(4))
        self.oppositeEdge = struct.unpack('>I', infile.read(4))
        self.oppositeFace = struct.unpack('>I', infile.read(4))
        self.flags = any(infile)  # TYPE_FLAGS
        self.paddingByte = struct.unpack('>B', infile.read(1))
        self.userEdgeCost = struct.unpack('>h', infile.read(2))
