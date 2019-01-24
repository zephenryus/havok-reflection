from .hkaiAstarEdgeFilter import hkaiAstarEdgeFilter


class hkaiDefaultAstarEdgeFilter(hkaiAstarEdgeFilter):
    edgeMaskLookupTable: int
    faceMaskLookupTable: int
    cellMaskLookupTable: int
