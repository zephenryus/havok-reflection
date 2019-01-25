from .hkpPhantom import hkpPhantom
from .hkAabb import hkAabb
from typing import List
from .common import get_array
import struct


class hkpAabbPhantom(hkpPhantom):
    aabb: hkAabb
    overlappingCollidables: List[any]
    orderDirty: bool

    def __init__(self, infile):
        self.aabb = hkAabb(infile)  # TYPE_STRUCT:TYPE_VOID
        self.overlappingCollidables = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.orderDirty = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} aabb={aabb}, overlappingCollidables=[{overlappingCollidables}], orderDirty={orderDirty}>".format(**{
            "class_name": self.__class__.__name__,
            "aabb": self.aabb,
            "overlappingCollidables": self.overlappingCollidables,
            "orderDirty": self.orderDirty,
        })
