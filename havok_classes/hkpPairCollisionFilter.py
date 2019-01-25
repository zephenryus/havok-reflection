from .hkpCollisionFilter import hkpCollisionFilter
from .hkpPairCollisionFilterMapPairFilterKeyOverrideType import hkpPairCollisionFilterMapPairFilterKeyOverrideType


class hkpPairCollisionFilter(hkpCollisionFilter):
    disabledPairs: hkpPairCollisionFilterMapPairFilterKeyOverrideType
    childFilter: any

    def __init__(self, infile):
        self.disabledPairs = hkpPairCollisionFilterMapPairFilterKeyOverrideType(infile)  # TYPE_STRUCT:TYPE_VOID
        self.childFilter = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} disabledPairs={disabledPairs}, childFilter={childFilter}>".format(**{
            "class_name": self.__class__.__name__,
            "disabledPairs": self.disabledPairs,
            "childFilter": self.childFilter,
        })
