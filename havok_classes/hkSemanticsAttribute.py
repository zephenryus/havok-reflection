from enum import Enum
from .enums import Semantics


class Semantics(Enum):
    UNKNOWN = 0
    DISTANCE = 1
    ANGLE = 2
    NORMAL = 3
    POSITION = 4
    COSINE_ANGLE = 5


class hkSemanticsAttribute(object):
    type: Semantics

    def __init__(self, infile):
        self.type = Semantics(infile)  # TYPE_ENUM
