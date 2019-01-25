from .hkpShapeCollection import hkpShapeCollection
from enum import Enum
from .hkpListShapeChildInfo import hkpListShapeChildInfo
import struct
from .common import vector4


class ListShapeFlags(Enum):
    ALL_FLAGS_CLEAR = 0
    DISABLE_SPU_CACHE_FOR_LIST_CHILD_INFO = 1


class hkpListShape(hkpShapeCollection):
    childInfo: hkpListShapeChildInfo
    flags: int
    numDisabledChildren: int
    aabbHalfExtents: vector4
    aabbCenter: vector4
    enabledChildren: int

    def __init__(self, infile):
        self.childInfo = hkpListShapeChildInfo(infile)  # TYPE_ARRAY
        self.flags = struct.unpack('>H', infile.read(2))
        self.numDisabledChildren = struct.unpack('>H', infile.read(2))
        self.aabbHalfExtents = struct.unpack('>4f', infile.read(16))
        self.aabbCenter = struct.unpack('>4f', infile.read(16))
        self.enabledChildren = struct.unpack('>I', infile.read(4))
