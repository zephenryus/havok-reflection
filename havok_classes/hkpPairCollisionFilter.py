from .hkpCollisionFilter import hkpCollisionFilter
from .hkpPairCollisionFilterMapPairFilterKeyOverrideType import hkpPairCollisionFilterMapPairFilterKeyOverrideType


class hkpPairCollisionFilter(hkpCollisionFilter):
    disabledPairs: hkpPairCollisionFilterMapPairFilterKeyOverrideType
    childFilter: hkpCollisionFilter

    def __init__(self, infile):
        self.disabledPairs = hkpPairCollisionFilterMapPairFilterKeyOverrideType(infile)  # TYPE_STRUCT
        self.childFilter = hkpCollisionFilter(infile)  # TYPE_POINTER
