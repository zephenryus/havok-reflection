from .hkpCollisionFilter import hkpCollisionFilter
import struct


class hkpGroupFilter(hkpCollisionFilter):
    nextFreeSystemGroup: int
    collisionLookupTable: int
    pad256: vector4

    def __init__(self, infile):
        self.nextFreeSystemGroup = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.collisionLookupTable = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.pad256 = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} nextFreeSystemGroup={nextFreeSystemGroup}, collisionLookupTable={collisionLookupTable}, pad256={pad256}>".format(**{
            "class_name": self.__class__.__name__,
            "nextFreeSystemGroup": self.nextFreeSystemGroup,
            "collisionLookupTable": self.collisionLookupTable,
            "pad256": self.pad256,
        })
