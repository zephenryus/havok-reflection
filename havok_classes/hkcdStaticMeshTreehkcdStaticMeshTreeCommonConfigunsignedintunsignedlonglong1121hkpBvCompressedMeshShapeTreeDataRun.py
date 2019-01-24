from .hkcdStaticMeshTreeBase import hkcdStaticMeshTreeBase
from enum import Enum
from .common import any
from .hkpBvCompressedMeshShapeTreeDataRun import hkpBvCompressedMeshShapeTreeDataRun


class TriangleMaterial(Enum):
    TM_SET_FROM_TRIANGLE_DATA_TYPE = 0
    TM_SET_FROM_PRIMITIVE_KEY = 1


class hkcdStaticMeshTreehkcdStaticMeshTreeCommonConfigunsignedintunsignedlonglong1121hkpBvCompressedMeshShapeTreeDataRun(hkcdStaticMeshTreeBase):
    packedVertices: any
    sharedVertices: any
    primitiveDataRuns: hkpBvCompressedMeshShapeTreeDataRun
