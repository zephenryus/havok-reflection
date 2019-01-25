from .hkReferencedObject import hkReferencedObject
from enum import Enum
import struct
from typing import List
from .common import get_array
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
    planes: List[hkcdPlanarGeometryPrimitivesPlane]
    cache: any
    criticalAccess: any

    def __init__(self, infile):
        self.offsetAndScale = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.planes = get_array(infile, hkcdPlanarGeometryPrimitivesPlane, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.cache = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.criticalAccess = any(infile)  # TYPE_POINTER:TYPE_VOID

    def __repr__(self):
        return "<{class_name} offsetAndScale={offsetAndScale}, planes=[{planes}], cache={cache}, criticalAccess={criticalAccess}>".format(**{
            "class_name": self.__class__.__name__,
            "offsetAndScale": self.offsetAndScale,
            "planes": self.planes,
            "cache": self.cache,
            "criticalAccess": self.criticalAccess,
        })
