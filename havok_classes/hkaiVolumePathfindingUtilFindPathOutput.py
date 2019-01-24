from .hkReferencedObject import hkReferencedObject
from .common import any
from .hkaiPathPathPoint import hkaiPathPathPoint
from .hkaiAstarOutputParameters import hkaiAstarOutputParameters


class hkaiVolumePathfindingUtilFindPathOutput(hkReferencedObject):
    visitedCells: any
    pathOut: hkaiPathPathPoint
    outputParameters: hkaiAstarOutputParameters
