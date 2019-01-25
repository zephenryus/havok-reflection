from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .common import vector4, any
import struct
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

    def __init__(self, infile):
        self.offsetAndScale = struct.unpack('>4f', infile.read(16))
        self.planes = hkcdPlanarGeometryPrimitivesPlane(infile)  # TYPE_ARRAY
        self.cache = any(infile)  # TYPE_POINTER
        self.criticalAccess = any(infile)  # TYPE_POINTER
