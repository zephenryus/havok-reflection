from .hkReferencedObject import hkReferencedObject
from enum import Enum
from typing import List
from .common import get_array
from .hkaiEdgePathEdge import hkaiEdgePathEdge
import struct


class PpivResult(Enum):
    PPIV_RESULT_SUCCESS = 0
    PPIV_RESULT_HIT_PATH_END = 1
    PPIV_RESULT_INVALID_PATH = 2


class hkaiEdgePath(hkReferencedObject):
    edges: List[hkaiEdgePathEdge]
    edgeData: List[int]
    edgeDataStriding: int
    leftTurnRadius: float
    rightTurnRadius: float
    characterRadius: float

    def __init__(self, infile):
        self.edges = get_array(infile, hkaiEdgePathEdge, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.edgeData = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32
        self.edgeDataStriding = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.leftTurnRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.rightTurnRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.characterRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} edges=[{edges}], edgeData=[{edgeData}], edgeDataStriding={edgeDataStriding}, leftTurnRadius={leftTurnRadius}, rightTurnRadius={rightTurnRadius}, characterRadius={characterRadius}>".format(**{
            "class_name": self.__class__.__name__,
            "edges": self.edges,
            "edgeData": self.edgeData,
            "edgeDataStriding": self.edgeDataStriding,
            "leftTurnRadius": self.leftTurnRadius,
            "rightTurnRadius": self.rightTurnRadius,
            "characterRadius": self.characterRadius,
        })
