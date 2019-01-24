from .hkpCollisionFilter import hkpCollisionFilter


class hkpGroupCollisionFilter(hkpCollisionFilter):
    noGroupCollisionEnabled: bool
    collisionGroups: int
