from enum import Enum


class Type(Enum):
    INVALID = 0
    TRIANGLE = 1
    QUAD = 2
    CUSTOM = 3
    NUM_TYPES = 4


class hkcdStaticMeshTreeBasePrimitive(object):
    indices: int
