from enum import Enum


class WalkableTriangleSettings(Enum):
    ONLY_FIX_WALKABLE = 0
    PREFER_WALKABLE = 1
    PREFER_UNWALKABLE = 2


class hkaiOverlappingTriangles(object):
    pass

    def __repr__(self):
        return "<{class_name} >".format(**{
            "class_name": self.__class__.__name__,
        })
