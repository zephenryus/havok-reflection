from enum import Enum
from .enums import ModelerType


class ModelerType(Enum):
    DEFAULT = 0
    LOCATOR = 1


class hkModelerNodeTypeAttribute(object):
    type: ModelerType

    def __init__(self, infile):
        self.type = ModelerType(infile)  # TYPE_ENUM
