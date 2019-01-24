from .hkMeshVertexBuffer import hkMeshVertexBuffer
from .hkMeshMaterial import hkMeshMaterial
from .hkMeshBoneIndexMapping import hkMeshBoneIndexMapping
from .enums import PrimitiveType, MeshSectionIndexType
from .common import any


class hkMeshSectionCinfo(object):
    vertexBuffer: hkMeshVertexBuffer
    material: hkMeshMaterial
    boneMatrixMap: hkMeshBoneIndexMapping
    primitiveType: PrimitiveType
    numPrimitives: int
    indexType: MeshSectionIndexType
    indices: any
    vertexStartIndex: int
    transformIndex: int
