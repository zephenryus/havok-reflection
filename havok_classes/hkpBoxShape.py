from .hkpConvexShape import hkpConvexShape
from .common import vector4


class hkpBoxShape(hkpConvexShape):
    halfExtents: vector4
