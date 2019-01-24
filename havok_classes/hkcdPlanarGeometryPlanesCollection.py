from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .common import vector4, any
from .hkcdPlanarGeometryPrimitivesPlane import hkcdPlanarGeometryPrimitivesPlane


class Bounds(Enum):
    BOUND_POS_X = 0
    BOUND_NEG_X = 1
    BOUND_POS_Y = 2
    BOUND_NEG_Y = 3
    BOUND_POS_Z = 4
    BOUND_NEG_Z = 5
    NUM_BOUNDS = 6


class hkcdPlanarGeometryPlanesCollection(hkReferencedObject):
    offsetAndScale: vector4
    planes: hkcdPlanarGeometryPrimitivesPlane
    cache: any
    criticalAccess: any
