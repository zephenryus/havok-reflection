from .hkpCollisionFilter import hkpCollisionFilter
from .common import vector4


class hkpGroupFilter(hkpCollisionFilter):
    nextFreeSystemGroup: int
    collisionLookupTable: int
    pad256: vector4
