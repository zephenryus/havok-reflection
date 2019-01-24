from .hkpConvexShape import hkpConvexShape
from enum import Enum
from .common import vector4


class RayHitType(Enum):
    HIT_CAP0 = 0
    HIT_CAP1 = 1
    HIT_BODY = 2


class hkpCapsuleShape(hkpConvexShape):
    vertexA: vector4
    vertexB: vector4
