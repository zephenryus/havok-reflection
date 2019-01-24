from .hkpShapePhantom import hkpShapePhantom
from .hkpSimpleShapePhantomCollisionDetail import hkpSimpleShapePhantomCollisionDetail


class hkpSimpleShapePhantom(hkpShapePhantom):
    collisionDetails: hkpSimpleShapePhantomCollisionDetail
    orderDirty: bool
