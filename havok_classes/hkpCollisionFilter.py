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
        self.prepad = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.type = hkpFilterType(infile)  # TYPE_ENUM:TYPE_UINT32
        self.postpad = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} prepad={prepad}, type={type}, postpad={postpad}>".format(**{
            "class_name": self.__class__.__name__,
            "prepad": self.prepad,
            "type": self.type,
            "postpad": self.postpad,
        })
