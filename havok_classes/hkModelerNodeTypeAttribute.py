from enum import Enum
from .enums import ModelerType


class ModelerType(Enum):
    DEFAULT = 0
    LOCATOR = 1


class hkModelerNodeTypeAttribute(object):
    type: ModelerType
