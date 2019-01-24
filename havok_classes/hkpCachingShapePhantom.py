from .hkpShapePhantom import hkpShapePhantom
from .common import any


class hkpCachingShapePhantom(hkpShapePhantom):
    collisionDetails: any
    orderDirty: bool
