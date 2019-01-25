from .hkcdStaticTreeTreehkcdStaticTreeDynamicStorage5 import hkcdStaticTreeTreehkcdStaticTreeDynamicStorage5
from enum import Enum
import struct
from .hkcdStaticMeshTreeBaseSection import hkcdStaticMeshTreeBaseSection
from .hkcdStaticMeshTreeBasePrimitive import hkcdStaticMeshTreeBasePrimitive
from .common import any


class CompressionMode(Enum):
    CM_GLOBAL = 0
    CM_LOCAL_4 = 1
    CM_LOCAL_2 = 2
    CM_AUTO = 3


class hkcdStaticMeshTreeBase(hkcdStaticTreeTreehkcdStaticTreeDynamicStorage5):
    numPrimitiveKeys: int
    bitsPerKey: int
    maxKeyValue: int
    sections: hkcdStaticMeshTreeBaseSection
    primitives: hkcdStaticMeshTreeBasePrimitive
    sharedVerticesIndex: any

    def __init__(self, infile):
        self.numPrimitiveKeys = struct.unpack('>i', infile.read(4))
        self.bitsPerKey = struct.unpack('>i', infile.read(4))
        self.maxKeyValue = struct.unpack('>I', infile.read(4))
        self.sections = hkcdStaticMeshTreeBaseSection(infile)  # TYPE_ARRAY
        self.primitives = hkcdStaticMeshTreeBasePrimitive(infile)  # TYPE_ARRAY
        self.sharedVerticesIndex = any(infile)  # TYPE_ARRAY
