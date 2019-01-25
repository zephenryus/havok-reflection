from .hkpCollisionFilter import hkpCollisionFilter
import struct
from .common import vector4


class hkpGroupFilter(hkpCollisionFilter):
    nextFreeSystemGroup: int
    collisionLookupTable: int
    pad256: vector4

    def __init__(self, infile):
        self.nextFreeSystemGroup = struct.unpack('>i', infile.read(4))
        self.collisionLookupTable = struct.unpack('>I', infile.read(4))
        self.pad256 = struct.unpack('>4f', infile.read(16))
