from .hkReferencedObject import hkReferencedObject
from enum import Enum
import struct
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

    def __init__(self, infile):
        self.prepad = struct.unpack('>I', infile.read(4))
        self.type = hkpFilterType(infile)  # TYPE_ENUM
        self.postpad = struct.unpack('>I', infile.read(4))
