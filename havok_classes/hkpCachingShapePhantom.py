from .hkpShapePhantom import hkpShapePhantom
from typing import List
from .common import get_array
import struct


class hkpCachingShapePhantom(hkpShapePhantom):
    collisionDetails: List[any]
    orderDirty: bool

    def __init__(self, infile):
        self.collisionDetails = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_VOID
        self.orderDirty = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} collisionDetails=[{collisionDetails}], orderDirty={orderDirty}>".format(**{
            "class_name": self.__class__.__name__,
            "collisionDetails": self.collisionDetails,
            "orderDirty": self.orderDirty,
        })
