from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .enums import IndexType
from typing import List
from .common import get_array
import struct


class IndexType(Enum):
    INDEX_TYPE_INVALID = 0
    INDEX_TYPE_TRI_LIST = 1
    INDEX_TYPE_TRI_STRIP = 2
    INDEX_TYPE_TRI_FAN = 3
    INDEX_TYPE_MAX_ID = 4


class hkxIndexBuffer(hkReferencedObject):
    indexType: IndexType
    indices16: List[int]
    indices32: List[int]
    vertexBaseOffset: int
    length: int

    def __init__(self, infile):
        self.indexType = IndexType(infile)  # TYPE_ENUM:TYPE_INT8
        self.indices16 = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.indices32 = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.vertexBaseOffset = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.length = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} indexType={indexType}, indices16=[{indices16}], indices32=[{indices32}], vertexBaseOffset={vertexBaseOffset}, length={length}>".format(**{
            "class_name": self.__class__.__name__,
            "indexType": self.indexType,
            "indices16": self.indices16,
            "indices32": self.indices32,
            "vertexBaseOffset": self.vertexBaseOffset,
            "length": self.length,
        })
