from .hkpConvexShape import hkpConvexShape
from .hkpConvexShape import hkpConvexShape


class hkpConvexListShape(hkpConvexShape):
	minDistanceToUseConvexHullForGetClosestPoints: float
	aabbHalfExtents: any
	aabbCenter: any
	useCachedAabb: bool
	childShapes: hkpConvexShape
