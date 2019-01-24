from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaiNavVolumeCell import hkaiNavVolumeCell
from .hkaiNavVolumeEdge import hkaiNavVolumeEdge
from .hkaiStreamingSet import hkaiStreamingSet
from .hkAabb import hkAabb
from .common import vector4


class Constants(Enum):
    INVALID_CELL_INDEX = 4294967295
    INVALID_EDGE_INDEX = 4294967295


class CellEdgeFlagBits(Enum):
    EDGE_EXTERNAL_OPPOSITE = 64


class hkaiNavVolume(hkReferencedObject):
    cells: hkaiNavVolumeCell
    edges: hkaiNavVolumeEdge
    streamingSets: hkaiStreamingSet
    aabb: hkAabb
    quantizationScale: vector4
    quantizationOffset: vector4
    res: int
    userData: int
