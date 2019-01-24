from .common import any


class hkaiNavMeshEdge(object):
    a: int
    b: int
    oppositeEdge: int
    oppositeFace: int
    flags: any
    paddingByte: int
    userEdgeCost: int
