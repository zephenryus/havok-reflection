from .hkpPhantom import hkpPhantom
from .hkAabb import hkAabb
from .common import any
import struct


class hkpAabbPhantom(hkpPhantom):
    aabb: hkAabb
    overlappingCollidables: any
    orderDirty: bool

    def __init__(self, infile):
        self.aabb = hkAabb(infile)  # TYPE_STRUCT
        self.overlappingCollidables = any(infile)  # TYPE_ARRAY
        self.orderDirty = struct.unpack('>?', infile.read(1))
