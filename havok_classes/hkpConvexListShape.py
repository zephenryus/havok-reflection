from .hkpConvexShape import hkpConvexShape
import struct
from typing import List
from .common import get_array


class hkpConvexListShape(hkpConvexShape):
    minDistanceToUseConvexHullForGetClosestPoints: float
    aabbHalfExtents: vector4
    aabbCenter: vector4
    useCachedAabb: bool
    childShapes: List[hkpConvexShape]

    def __init__(self, infile):
        self.minDistanceToUseConvexHullForGetClosestPoints = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.aabbHalfExtents = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.aabbCenter = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.useCachedAabb = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.childShapes = get_array(infile, hkpConvexShape, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} minDistanceToUseConvexHullForGetClosestPoints={minDistanceToUseConvexHullForGetClosestPoints}, aabbHalfExtents={aabbHalfExtents}, aabbCenter={aabbCenter}, useCachedAabb={useCachedAabb}, childShapes=[{childShapes}]>".format(**{
            "class_name": self.__class__.__name__,
            "minDistanceToUseConvexHullForGetClosestPoints": self.minDistanceToUseConvexHullForGetClosestPoints,
            "aabbHalfExtents": self.aabbHalfExtents,
            "aabbCenter": self.aabbCenter,
            "useCachedAabb": self.useCachedAabb,
            "childShapes": self.childShapes,
        })
