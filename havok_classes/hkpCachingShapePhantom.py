from .hkpShapePhantom import hkpShapePhantom
from .common import any
import struct


class hkpCachingShapePhantom(hkpShapePhantom):
    collisionDetails: any
    orderDirty: bool

    def __init__(self, infile):
        self.collisionDetails = any(infile)  # TYPE_ARRAY
        self.orderDirty = struct.unpack('>?', infile.read(1))
