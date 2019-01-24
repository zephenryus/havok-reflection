from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaiEdgePathEdge import hkaiEdgePathEdge
from .common import any


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
