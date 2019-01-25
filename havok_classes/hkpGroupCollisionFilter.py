from .hkpCollisionFilter import hkpCollisionFilter
import struct


class hkpGroupCollisionFilter(hkpCollisionFilter):
    noGroupCollisionEnabled: bool
    collisionGroups: int

    def __init__(self, infile):
        self.noGroupCollisionEnabled = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.collisionGroups = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} noGroupCollisionEnabled={noGroupCollisionEnabled}, collisionGroups={collisionGroups}>".format(**{
            "class_name": self.__class__.__name__,
            "noGroupCollisionEnabled": self.noGroupCollisionEnabled,
            "collisionGroups": self.collisionGroups,
        })
