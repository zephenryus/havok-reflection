from enum import Enum
from .enums import ArrayType


class ArrayType(Enum):
    NONE = 0
    POINTSOUP = 1
    ENTITIES = 2


class hkArrayTypeAttribute(object):
    type: ArrayType

    def __init__(self, infile):
        self.type = ArrayType(infile)  # TYPE_ENUM
