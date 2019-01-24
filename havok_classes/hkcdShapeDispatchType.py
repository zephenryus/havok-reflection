from enum import Enum


class ShapeDispatchTypeEnum(Enum):
    CONVEX_IMPLICIT = 0
    CONVEX = 1
    HEIGHT_FIELD = 2
    COMPOSITE = 3
    USER = 4
    NUM_DISPATCH_TYPES = 5


class hkcdShapeDispatchType(object):
    pass
