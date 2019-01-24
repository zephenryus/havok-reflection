from .hkReferencedObject import hkReferencedObject
from enum import Enum


class ConvexListCollisionType(Enum):
    TREAT_CONVEX_LIST_AS_NORMAL = 0
    TREAT_CONVEX_LIST_AS_LIST = 1
    TREAT_CONVEX_LIST_AS_CONVEX = 2


class hkpConvexListFilter(hkReferencedObject):
    pass
