from .hkcdStaticTreeTreehkcdStaticTreeDynamicStorage5 import hkcdStaticTreeTreehkcdStaticTreeDynamicStorage5
from enum import Enum
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
