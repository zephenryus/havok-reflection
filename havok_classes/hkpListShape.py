from .hkpShapeCollection import hkpShapeCollection
from enum import Enum
from typing import List
from .common import get_array
from .hkpListShapeChildInfo import hkpListShapeChildInfo
import struct


class ListShapeFlags(Enum):
    ALL_FLAGS_CLEAR = 0
    DISABLE_SPU_CACHE_FOR_LIST_CHILD_INFO = 1


class hkpListShape(hkpShapeCollection):
    childInfo: List[hkpListShapeChildInfo]
    flags: int
    numDisabledChildren: int
    aabbHalfExtents: vector4
    aabbCenter: vector4
    enabledChildren: int

    def __init__(self, infile):
        self.childInfo = get_array(infile, hkpListShapeChildInfo, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.flags = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.numDisabledChildren = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.aabbHalfExtents = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.aabbCenter = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.enabledChildren = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} childInfo=[{childInfo}], flags={flags}, numDisabledChildren={numDisabledChildren}, aabbHalfExtents={aabbHalfExtents}, aabbCenter={aabbCenter}, enabledChildren={enabledChildren}>".format(**{
            "class_name": self.__class__.__name__,
            "childInfo": self.childInfo,
            "flags": self.flags,
            "numDisabledChildren": self.numDisabledChildren,
            "aabbHalfExtents": self.aabbHalfExtents,
            "aabbCenter": self.aabbCenter,
            "enabledChildren": self.enabledChildren,
        })
