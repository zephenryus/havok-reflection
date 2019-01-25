from .hkpCollisionFilter import hkpCollisionFilter


class hkpConstrainedSystemFilter(hkpCollisionFilter):
    otherFilter: hkpCollisionFilter

    def __init__(self, infile):
        self.otherFilter = hkpCollisionFilter(infile)  # TYPE_POINTER
