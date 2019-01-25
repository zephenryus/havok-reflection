from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .enums import IndexType
from .common import any
import struct


class IndexType(Enum):
    INDEX_TYPE_INVALID = 0
    INDEX_TYPE_TRI_LIST = 1
    INDEX_TYPE_TRI_STRIP = 2
    INDEX_TYPE_TRI_FAN = 3
    INDEX_TYPE_MAX_ID = 4


class hkxIndexBuffer(hkReferencedObject):
    indexType: IndexType
    indices16: any
    indices32: any
    vertexBaseOffset: int
    length: int

    def __init__(self, infile):
        self.indexType = IndexType(infile)  # TYPE_ENUM
        self.indices16 = any(infile)  # TYPE_ARRAY
        self.indices32 = any(infile)  # TYPE_ARRAY
        self.vertexBaseOffset = struct.unpack('>I', infile.read(4))
        self.length = struct.unpack('>I', infile.read(4))
