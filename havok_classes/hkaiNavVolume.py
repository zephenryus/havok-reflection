from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaiNavVolumeCell import hkaiNavVolumeCell
from .hkaiNavVolumeEdge import hkaiNavVolumeEdge
from .hkaiStreamingSet import hkaiStreamingSet
from .hkAabb import hkAabb
from .common import vector4
import struct


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

    def __init__(self, infile):
        self.cells = hkaiNavVolumeCell(infile)  # TYPE_ARRAY
        self.edges = hkaiNavVolumeEdge(infile)  # TYPE_ARRAY
        self.streamingSets = hkaiStreamingSet(infile)  # TYPE_ARRAY
        self.aabb = hkAabb(infile)  # TYPE_STRUCT
        self.quantizationScale = struct.unpack('>4f', infile.read(16))
        self.quantizationOffset = struct.unpack('>4f', infile.read(16))
        self.res = struct.unpack('>i', infile.read(4))
        self.userData = struct.unpack('>L', infile.read(8))
