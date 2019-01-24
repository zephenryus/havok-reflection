from .hkpConvexShape import hkpConvexShape
from .common import vector4, any
from .hkpConvexVerticesConnectivity import hkpConvexVerticesConnectivity


class hkpConvexVerticesShape(hkpConvexShape):
    aabbHalfExtents: vector4
    aabbCenter: vector4
    rotatedVertices: any
    numVertices: int
    useSpuBuffer: bool
    planeEquations: any
    connectivity: hkpConvexVerticesConnectivity
