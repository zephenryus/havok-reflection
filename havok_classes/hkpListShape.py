from .hkpShapeCollection import hkpShapeCollection
from enum import Enum
from .hkpListShapeChildInfo import hkpListShapeChildInfo
from .common import vector4


class ListShapeFlags(Enum):
    ALL_FLAGS_CLEAR = 0
    DISABLE_SPU_CACHE_FOR_LIST_CHILD_INFO = 1


class hkpListShape(hkpShapeCollection):
    childInfo: hkpListShapeChildInfo
    flags: int
    numDisabledChildren: int
    aabbHalfExtents: vector4
    aabbCenter: vector4
    enabledChildren: int
