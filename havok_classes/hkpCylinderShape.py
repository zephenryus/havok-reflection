from .hkpConvexShape import hkpConvexShape


class hkpCylinderShape(hkpConvexShape):
	cylRadius: float
	cylBaseRadiusFactorForHeightFieldCollisions: float
	vertexA: any
	vertexB: any
	perpendicular1: any
	perpendicular2: any
