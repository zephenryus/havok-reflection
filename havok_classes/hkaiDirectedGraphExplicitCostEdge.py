import struct
from .common import any


class hkaiDirectedGraphExplicitCostEdge(object):
    cost: int
    flags: any
    target: int

    def __init__(self, infile):
        self.cost = struct.unpack('>h', infile.read(2))
        self.flags = any(infile)  # TYPE_FLAGS
        self.target = struct.unpack('>I', infile.read(4))
