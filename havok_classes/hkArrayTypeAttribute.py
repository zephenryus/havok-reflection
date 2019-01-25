from enum import Enum
from .enums import ArrayType


class ArrayType(Enum):
    NONE = 0
    POINTSOUP = 1
    ENTITIES = 2


class hkArrayTypeAttribute(object):
    type: ArrayType

    def __init__(self, infile):
        self.type = ArrayType(infile)  # TYPE_ENUM:TYPE_INT8

    def __repr__(self):
        return "<{class_name} type={type}>".format(**{
            "class_name": self.__class__.__name__,
            "type": self.type,
        })
