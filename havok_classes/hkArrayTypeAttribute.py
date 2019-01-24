from enum import Enum
from .enums import ArrayType


class ArrayType(Enum):
    NONE = 0
    POINTSOUP = 1
    ENTITIES = 2


class hkArrayTypeAttribute(object):
    type: ArrayType
