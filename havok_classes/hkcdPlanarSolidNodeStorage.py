from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkcdPlanarSolidNode import hkcdPlanarSolidNode
from .hkAabb import hkAabb
import struct


class hkcdPlanarSolidNodeStorage(hkReferencedObject):
    storage: List[hkcdPlanarSolidNode]
    aabbs: List[hkAabb]
    firstFreeNodeId: int

    def __init__(self, infile):
        self.storage = get_array(infile, hkcdPlanarSolidNode, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.aabbs = get_array(infile, hkAabb, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.firstFreeNodeId = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} storage=[{storage}], aabbs=[{aabbs}], firstFreeNodeId={firstFreeNodeId}>".format(**{
            "class_name": self.__class__.__name__,
            "storage": self.storage,
            "aabbs": self.aabbs,
            "firstFreeNodeId": self.firstFreeNodeId,
        })
