from .hkpConvexShape import hkpConvexShape
from .hkpConvexVerticesConnectivity import hkpConvexVerticesConnectivity


class hkpConvexVerticesShape(hkpConvexShape):
	aabbHalfExtents: any
	aabbCenter: any
	rotatedVertices: any
	numVertices: int
	useSpuBuffer: bool
	planeEquations: any
	connectivity: hkpConvexVerticesConnectivity
