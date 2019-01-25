from .hkpCollisionFilter import hkpCollisionFilter


class hkpConstrainedSystemFilter(hkpCollisionFilter):
    otherFilter: any

    def __init__(self, infile):
        self.otherFilter = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} otherFilter={otherFilter}>".format(**{
            "class_name": self.__class__.__name__,
            "otherFilter": self.otherFilter,
        })
