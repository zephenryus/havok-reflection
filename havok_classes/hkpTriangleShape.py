from .hkpConvexShape import hkpConvexShape
from .enums import WeldingType
from .common import vector4


class hkpTriangleShape(hkpConvexShape):
    weldingInfo: int
    weldingType: WeldingType
    isExtruded: int
    vertexA: vector4
    vertexB: vector4
    vertexC: vector4
    extrusion: vector4
