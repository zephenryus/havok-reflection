from .hkpCollisionFilter import hkpCollisionFilter


class hkpConstrainedSystemFilter(hkpCollisionFilter):
    otherFilter: hkpCollisionFilter
