from .hkcdStaticTreeTreehkcdStaticTreeDynamicStorage5 import hkcdStaticTreeTreehkcdStaticTreeDynamicStorage5
from enum import Enum
import struct
from typing import List
from .common import get_array
from .hkcdStaticMeshTreeBaseSection import hkcdStaticMeshTreeBaseSection
from .hkcdStaticMeshTreeBasePrimitive import hkcdStaticMeshTreeBasePrimitive


class CompressionMode(Enum):
    CM_GLOBAL = 0
    CM_LOCAL_4 = 1
    CM_LOCAL_2 = 2
    CM_AUTO = 3


class hkcdStaticMeshTreeBase(hkcdStaticTreeTreehkcdStaticTreeDynamicStorage5):
    numPrimitiveKeys: int
    bitsPerKey: int
    maxKeyValue: int
    sections: List[hkcdStaticMeshTreeBaseSection]
    primitives: List[hkcdStaticMeshTreeBasePrimitive]
    sharedVerticesIndex: List[int]

    def __init__(self, infile):
        self.numPrimitiveKeys = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.bitsPerKey = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.maxKeyValue = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.sections = get_array(infile, hkcdStaticMeshTreeBaseSection, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.primitives = get_array(infile, hkcdStaticMeshTreeBasePrimitive, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.sharedVerticesIndex = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16

    def __repr__(self):
        return "<{class_name} numPrimitiveKeys={numPrimitiveKeys}, bitsPerKey={bitsPerKey}, maxKeyValue={maxKeyValue}, sections=[{sections}], primitives=[{primitives}], sharedVerticesIndex=[{sharedVerticesIndex}]>".format(**{
            "class_name": self.__class__.__name__,
            "numPrimitiveKeys": self.numPrimitiveKeys,
            "bitsPerKey": self.bitsPerKey,
            "maxKeyValue": self.maxKeyValue,
            "sections": self.sections,
            "primitives": self.primitives,
            "sharedVerticesIndex": self.sharedVerticesIndex,
        })
