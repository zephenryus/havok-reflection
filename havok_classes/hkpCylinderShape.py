from .hkpConvexShape import hkpConvexShape
from enum import Enum
from .common import vector4


class VertexIdEncoding(Enum):
    VERTEX_ID_ENCODING_IS_BASE_A_SHIFT = 7
    VERTEX_ID_ENCODING_SIN_SIGN_SHIFT = 6
    VERTEX_ID_ENCODING_COS_SIGN_SHIFT = 5
    VERTEX_ID_ENCODING_IS_SIN_LESSER_SHIFT = 4
    VERTEX_ID_ENCODING_VALUE_MASK = 15


class hkpCylinderShape(hkpConvexShape):
    cylRadius: float
    cylBaseRadiusFactorForHeightFieldCollisions: float
    vertexA: vector4
    vertexB: vector4
    perpendicular1: vector4
    perpendicular2: vector4
