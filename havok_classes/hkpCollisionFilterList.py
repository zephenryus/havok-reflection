from .hkpCollisionFilter import hkpCollisionFilter


class hkpCollisionFilterList(hkpCollisionFilter):
    collisionFilters: hkpCollisionFilter

    def __init__(self, infile):
        self.collisionFilters = hkpCollisionFilter(infile)  # TYPE_ARRAY
