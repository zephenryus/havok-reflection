from .hkpCollisionFilter import hkpCollisionFilter
from .hkpEntity import hkpEntity


class hkpDisableEntityCollisionFilter(hkpCollisionFilter):
    disabledEntities: hkpEntity

    def __init__(self, infile):
        self.disabledEntities = hkpEntity(infile)  # TYPE_ARRAY
