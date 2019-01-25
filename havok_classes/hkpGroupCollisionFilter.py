from .hkpCollisionFilter import hkpCollisionFilter
import struct


class hkpGroupCollisionFilter(hkpCollisionFilter):
    noGroupCollisionEnabled: bool
    collisionGroups: int

    def __init__(self, infile):
        self.noGroupCollisionEnabled = struct.unpack('>?', infile.read(1))
        self.collisionGroups = struct.unpack('>I', infile.read(4))
