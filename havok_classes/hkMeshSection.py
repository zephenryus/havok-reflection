from enum import Enum
from .enums import PrimitiveType, MeshSectionIndexType
from .common import any
from .hkMeshVertexBuffer import hkMeshVertexBuffer
from .hkMeshMaterial import hkMeshMaterial
from .hkMeshBoneIndexMapping import hkMeshBoneIndexMapping


class MeshSectionIndexType(Enum):
    INDEX_TYPE_NONE = 0
    INDEX_TYPE_UINT16 = 1
    INDEX_TYPE_UINT32 = 2


class PrimitiveType(Enum):
    PRIMITIVE_TYPE_UNKNOWN = 0
    PRIMITIVE_TYPE_POINT_LIST = 1
    PRIMITIVE_TYPE_LINE_LIST = 2
    PRIMITIVE_TYPE_TRIANGLE_LIST = 3
    PRIMITIVE_TYPE_TRIANGLE_STRIP = 4


class hkMeshSection(object):
    primitiveType: PrimitiveType
    numPrimitives: int
    numIndices: int
    vertexStartIndex: int
    transformIndex: int
    indexType: MeshSectionIndexType
    indices: any
    vertexBuffer: hkMeshVertexBuffer
    material: hkMeshMaterial
    boneMatrixMap: hkMeshBoneIndexMapping
    sectionIndex: int
