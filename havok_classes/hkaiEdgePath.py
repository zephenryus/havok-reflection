from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaiEdgePathEdge import hkaiEdgePathEdge
from .common import any
import struct


class PpivResult(Enum):
    PPIV_RESULT_SUCCESS = 0
    PPIV_RESULT_HIT_PATH_END = 1
    PPIV_RESULT_INVALID_PATH = 2


class hkaiEdgePath(hkReferencedObject):
    edges: hkaiEdgePathEdge
    edgeData: any
    edgeDataStriding: int
    leftTurnRadius: float
    rightTurnRadius: float
    characterRadius: float

    def __init__(self, infile):
        self.edges = hkaiEdgePathEdge(infile)  # TYPE_ARRAY
        self.edgeData = any(infile)  # TYPE_ARRAY
        self.edgeDataStriding = struct.unpack('>i', infile.read(4))
        self.leftTurnRadius = struct.unpack('>f', infile.read(4))
        self.rightTurnRadius = struct.unpack('>f', infile.read(4))
        self.characterRadius = struct.unpack('>f', infile.read(4))
