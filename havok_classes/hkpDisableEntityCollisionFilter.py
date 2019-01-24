from .hkpCollisionFilter import hkpCollisionFilter
from .hkpEntity import hkpEntity


class hkpDisableEntityCollisionFilter(hkpCollisionFilter):
    disabledEntities: hkpEntity
