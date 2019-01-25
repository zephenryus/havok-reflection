from .hkpShapePhantom import hkpShapePhantom
from .hkpSimpleShapePhantomCollisionDetail import hkpSimpleShapePhantomCollisionDetail
import struct


class hkpSimpleShapePhantom(hkpShapePhantom):
    collisionDetails: hkpSimpleShapePhantomCollisionDetail
    orderDirty: bool

    def __init__(self, infile):
        self.collisionDetails = hkpSimpleShapePhantomCollisionDetail(infile)  # TYPE_ARRAY
        self.orderDirty = struct.unpack('>?', infile.read(1))
