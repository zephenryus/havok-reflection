from .hkMeshVertexBuffer import hkMeshVertexBuffer
from .hkMeshMaterial import hkMeshMaterial
from .hkMeshBoneIndexMapping import hkMeshBoneIndexMapping
from .enums import PrimitiveType, MeshSectionIndexType
import struct
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

    def __init__(self, infile):
        self.vertexBuffer = hkMeshVertexBuffer(infile)  # TYPE_POINTER
        self.material = hkMeshMaterial(infile)  # TYPE_POINTER
        self.boneMatrixMap = hkMeshBoneIndexMapping(infile)  # TYPE_STRUCT
        self.primitiveType = PrimitiveType(infile)  # TYPE_ENUM
        self.numPrimitives = struct.unpack('>i', infile.read(4))
        self.indexType = MeshSectionIndexType(infile)  # TYPE_ENUM
        self.indices = any(infile)  # TYPE_POINTER
        self.vertexStartIndex = struct.unpack('>i', infile.read(4))
        self.transformIndex = struct.unpack('>i', infile.read(4))
