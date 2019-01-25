from .hkMeshVertexBuffer import hkMeshVertexBuffer
from .hkMeshMaterial import hkMeshMaterial
from .hkMeshBoneIndexMapping import hkMeshBoneIndexMapping
from .enums import PrimitiveType, MeshSectionIndexType
import struct


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

    def __init__(self, infile):
        self.vertexBuffer = hkMeshVertexBuffer(infile)  # TYPE_POINTER
        self.material = hkMeshMaterial(infile)  # TYPE_POINTER
        self.boneMatrixMap = hkMeshBoneIndexMapping(infile)  # TYPE_STRUCT
        self.primitiveType = PrimitiveType(infile)  # TYPE_ENUM
        self.numPrimitives = struct.unpack('>i', infile.read(4))
        self.indexType = MeshSectionIndexType(infile)  # TYPE_ENUM
        self.vertexStartIndex = struct.unpack('>i', infile.read(4))
        self.transformIndex = struct.unpack('>i', infile.read(4))
        self.indexBufferOffset = struct.unpack('>i', infile.read(4))
