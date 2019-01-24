from .hkpConvexShape import hkpConvexShape
from .common import vector4


class hkpConvexListShape(hkpConvexShape):
    minDistanceToUseConvexHullForGetClosestPoints: float
    aabbHalfExtents: vector4
    aabbCenter: vector4
    useCachedAabb: bool
    childShapes: hkpConvexShape
