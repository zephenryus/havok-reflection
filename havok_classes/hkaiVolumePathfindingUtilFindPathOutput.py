from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkaiPathPathPoint import hkaiPathPathPoint
from .hkaiAstarOutputParameters import hkaiAstarOutputParameters


class hkaiVolumePathfindingUtilFindPathOutput(hkReferencedObject):
    visitedCells: List[int]
    pathOut: List[hkaiPathPathPoint]
    outputParameters: hkaiAstarOutputParameters

    def __init__(self, infile):
        self.visitedCells = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.pathOut = get_array(infile, hkaiPathPathPoint, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.outputParameters = hkaiAstarOutputParameters(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} visitedCells=[{visitedCells}], pathOut=[{pathOut}], outputParameters={outputParameters}>".format(**{
            "class_name": self.__class__.__name__,
            "visitedCells": self.visitedCells,
            "pathOut": self.pathOut,
            "outputParameters": self.outputParameters,
        })
