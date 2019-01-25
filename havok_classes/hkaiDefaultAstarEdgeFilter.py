from .hkaiAstarEdgeFilter import hkaiAstarEdgeFilter
import struct


class hkaiDefaultAstarEdgeFilter(hkaiAstarEdgeFilter):
    edgeMaskLookupTable: int
    faceMaskLookupTable: int
    cellMaskLookupTable: int

    def __init__(self, infile):
        self.edgeMaskLookupTable = struct.unpack('>I', infile.read(4))
        self.faceMaskLookupTable = struct.unpack('>I', infile.read(4))
        self.cellMaskLookupTable = struct.unpack('>I', infile.read(4))
