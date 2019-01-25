from .hkpCollisionFilter import hkpCollisionFilter
from typing import List
from .common import get_array


class hkpCollisionFilterList(hkpCollisionFilter):
    collisionFilters: List[hkpCollisionFilter]

    def __init__(self, infile):
        self.collisionFilters = get_array(infile, hkpCollisionFilter, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} collisionFilters=[{collisionFilters}]>".format(**{
            "class_name": self.__class__.__name__,
            "collisionFilters": self.collisionFilters,
        })
