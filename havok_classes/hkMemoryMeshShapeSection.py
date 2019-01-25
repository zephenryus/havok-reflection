from .hkMeshVertexBuffer import hkMeshVertexBuffer
from .hkMeshMaterial import hkMeshMaterial
from .hkMeshBoneIndexMapping import hkMeshBoneIndexMapping
from .enums import PrimitiveType, MeshSectionIndexType
import struct


class hkMemoryMeshShapeSection(object):
    vertexBuffer: any
    material: any
    boneMatrixMap: hkMeshBoneIndexMapping
    primitiveType: PrimitiveType
    numPrimitives: int
    indexType: MeshSectionIndexType
    vertexStartIndex: int
    transformIndex: int
    indexBufferOffset: int

    def __init__(self, infile):
        self.vertexBuffer = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.material = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.boneMatrixMap = hkMeshBoneIndexMapping(infile)  # TYPE_STRUCT:TYPE_VOID
        self.primitiveType = PrimitiveType(infile)  # TYPE_ENUM:TYPE_UINT8
        self.numPrimitives = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.indexType = MeshSectionIndexType(infile)  # TYPE_ENUM:TYPE_UINT8
        self.vertexStartIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.transformIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.indexBufferOffset = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} vertexBuffer={vertexBuffer}, material={material}, boneMatrixMap={boneMatrixMap}, primitiveType={primitiveType}, numPrimitives={numPrimitives}, indexType={indexType}, vertexStartIndex={vertexStartIndex}, transformIndex={transformIndex}, indexBufferOffset={indexBufferOffset}>".format(**{
            "class_name": self.__class__.__name__,
            "vertexBuffer": self.vertexBuffer,
            "material": self.material,
            "boneMatrixMap": self.boneMatrixMap,
            "primitiveType": self.primitiveType,
            "numPrimitives": self.numPrimitives,
            "indexType": self.indexType,
            "vertexStartIndex": self.vertexStartIndex,
            "transformIndex": self.transformIndex,
            "indexBufferOffset": self.indexBufferOffset,
        })
