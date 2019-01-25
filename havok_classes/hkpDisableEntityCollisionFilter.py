from .hkpCollisionFilter import hkpCollisionFilter
from typing import List
from .common import get_array
from .hkpEntity import hkpEntity


class hkpDisableEntityCollisionFilter(hkpCollisionFilter):
    disabledEntities: List[hkpEntity]

    def __init__(self, infile):
        self.disabledEntities = get_array(infile, hkpEntity, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} disabledEntities=[{disabledEntities}]>".format(**{
            "class_name": self.__class__.__name__,
            "disabledEntities": self.disabledEntities,
        })
