from .hkaiAstarEdgeFilter import hkaiAstarEdgeFilter
import struct


class hkaiDefaultAstarEdgeFilter(hkaiAstarEdgeFilter):
    edgeMaskLookupTable: int
    faceMaskLookupTable: int
    cellMaskLookupTable: int

    def __init__(self, infile):
        self.edgeMaskLookupTable = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.faceMaskLookupTable = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.cellMaskLookupTable = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} edgeMaskLookupTable={edgeMaskLookupTable}, faceMaskLookupTable={faceMaskLookupTable}, cellMaskLookupTable={cellMaskLookupTable}>".format(**{
            "class_name": self.__class__.__name__,
            "edgeMaskLookupTable": self.edgeMaskLookupTable,
            "faceMaskLookupTable": self.faceMaskLookupTable,
            "cellMaskLookupTable": self.cellMaskLookupTable,
        })
