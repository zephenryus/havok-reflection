from enum import Enum
from .enums import PrimitiveType, MeshSectionIndexType
import struct
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
    vertexBuffer: any
    material: any
    boneMatrixMap: any
    sectionIndex: int

    def __init__(self, infile):
        self.primitiveType = PrimitiveType(infile)  # TYPE_ENUM:TYPE_UINT8
        self.numPrimitives = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numIndices = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.vertexStartIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.transformIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.indexType = MeshSectionIndexType(infile)  # TYPE_ENUM:TYPE_UINT8
        self.indices = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.vertexBuffer = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.material = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.boneMatrixMap = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.sectionIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} primitiveType={primitiveType}, numPrimitives={numPrimitives}, numIndices={numIndices}, vertexStartIndex={vertexStartIndex}, transformIndex={transformIndex}, indexType={indexType}, indices={indices}, vertexBuffer={vertexBuffer}, material={material}, boneMatrixMap={boneMatrixMap}, sectionIndex={sectionIndex}>".format(**{
            "class_name": self.__class__.__name__,
            "primitiveType": self.primitiveType,
            "numPrimitives": self.numPrimitives,
            "numIndices": self.numIndices,
            "vertexStartIndex": self.vertexStartIndex,
            "transformIndex": self.transformIndex,
            "indexType": self.indexType,
            "indices": self.indices,
            "vertexBuffer": self.vertexBuffer,
            "material": self.material,
            "boneMatrixMap": self.boneMatrixMap,
            "sectionIndex": self.sectionIndex,
        })
