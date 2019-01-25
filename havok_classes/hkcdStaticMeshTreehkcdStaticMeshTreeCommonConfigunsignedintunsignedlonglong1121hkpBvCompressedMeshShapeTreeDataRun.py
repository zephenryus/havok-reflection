from .hkcdStaticMeshTreeBase import hkcdStaticMeshTreeBase
from enum import Enum
from typing import List
from .common import get_array
from .hkpBvCompressedMeshShapeTreeDataRun import hkpBvCompressedMeshShapeTreeDataRun


class TriangleMaterial(Enum):
    TM_SET_FROM_TRIANGLE_DATA_TYPE = 0
    TM_SET_FROM_PRIMITIVE_KEY = 1


class hkcdStaticMeshTreehkcdStaticMeshTreeCommonConfigunsignedintunsignedlonglong1121hkpBvCompressedMeshShapeTreeDataRun(hkcdStaticMeshTreeBase):
    packedVertices: List[int]
    sharedVertices: List[int]
    primitiveDataRuns: List[hkpBvCompressedMeshShapeTreeDataRun]

    def __init__(self, infile):
        self.packedVertices = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.sharedVertices = get_array(infile, int, 8)  # TYPE_ARRAY:TYPE_UINT64
        self.primitiveDataRuns = get_array(infile, hkpBvCompressedMeshShapeTreeDataRun, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} packedVertices=[{packedVertices}], sharedVertices=[{sharedVertices}], primitiveDataRuns=[{primitiveDataRuns}]>".format(**{
            "class_name": self.__class__.__name__,
            "packedVertices": self.packedVertices,
            "sharedVertices": self.sharedVertices,
            "primitiveDataRuns": self.primitiveDataRuns,
        })
