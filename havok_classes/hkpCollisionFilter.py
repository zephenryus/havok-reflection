from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .enums import hkpFilterType


class hkpFilterType(Enum):
    HK_FILTER_UNKNOWN = 0
    HK_FILTER_NULL = 1
    HK_FILTER_GROUP = 2
    HK_FILTER_LIST = 3
    HK_FILTER_CUSTOM = 4
    HK_FILTER_PAIR = 5
    HK_FILTER_CONSTRAINT = 6


class hkpCollisionFilter(hkReferencedObject):
    prepad: int
    type: hkpFilterType
    postpad: int
