from enum import Enum
from .enums import ModelerType


class ModelerType(Enum):
    DEFAULT = 0
    LOCATOR = 1


class hkModelerNodeTypeAttribute(object):
    type: ModelerType

    def __init__(self, infile):
        self.type = ModelerType(infile)  # TYPE_ENUM:TYPE_INT8

    def __repr__(self):
        return "<{class_name} type={type}>".format(**{
            "class_name": self.__class__.__name__,
            "type": self.type,
        })
