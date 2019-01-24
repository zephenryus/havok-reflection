from .hkMeshVertexBuffer import hkMeshVertexBuffer
from .hkMeshMaterial import hkMeshMaterial
from .hkMeshBoneIndexMapping import hkMeshBoneIndexMapping
from .enums import PrimitiveType, MeshSectionIndexType


class hkMemoryMeshShapeSection(object):
    vertexBuffer: hkMeshVertexBuffer
    material: hkMeshMaterial
    boneMatrixMap: hkMeshBoneIndexMapping
    primitiveType: PrimitiveType
    numPrimitives: int
    indexType: MeshSectionIndexType
    vertexStartIndex: int
    transformIndex: int
    indexBufferOffset: int
