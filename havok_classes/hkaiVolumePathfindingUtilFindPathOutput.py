from .hkReferencedObject import hkReferencedObject
from .common import any
from .hkaiPathPathPoint import hkaiPathPathPoint
from .hkaiAstarOutputParameters import hkaiAstarOutputParameters


class hkaiVolumePathfindingUtilFindPathOutput(hkReferencedObject):
    visitedCells: any
    pathOut: hkaiPathPathPoint
    outputParameters: hkaiAstarOutputParameters

    def __init__(self, infile):
        self.visitedCells = any(infile)  # TYPE_ARRAY
        self.pathOut = hkaiPathPathPoint(infile)  # TYPE_ARRAY
        self.outputParameters = hkaiAstarOutputParameters(infile)  # TYPE_STRUCT
