from .hkReferencedObject import hkReferencedObject
from .hkcdPlanarSolidNode import hkcdPlanarSolidNode
from .hkAabb import hkAabb
import struct


class hkcdPlanarSolidNodeStorage(hkReferencedObject):
    storage: hkcdPlanarSolidNode
    aabbs: hkAabb
    firstFreeNodeId: int

    def __init__(self, infile):
        self.storage = hkcdPlanarSolidNode(infile)  # TYPE_ARRAY
        self.aabbs = hkAabb(infile)  # TYPE_ARRAY
        self.firstFreeNodeId = struct.unpack('>I', infile.read(4))
