from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .enums import EdgeFilterType


class EdgeFilterType(Enum):
    EDGE_FILTER_DEFAULT = 0
    EDGE_FILTER_USER = 1


class hkaiAstarEdgeFilter(hkReferencedObject):
    type: EdgeFilterType

    def __init__(self, infile):
        self.type = EdgeFilterType(infile)  # TYPE_ENUM
