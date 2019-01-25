from .hkpShapeCollection import hkpShapeCollection
from enum import Enum
import struct
from .enums import WeldingType, MaterialType
from .common import any
from .hkpCompressedMeshShapeBigTriangle import hkpCompressedMeshShapeBigTriangle
from .hkpCompressedMeshShapeChunk import hkpCompressedMeshShapeChunk
from .hkpCompressedMeshShapeConvexPiece import hkpCompressedMeshShapeConvexPiece
from .hkAabb import hkAabb
from .hkpNamedMeshMaterial import hkpNamedMeshMaterial


class MaterialType(Enum):
    MATERIAL_NONE = 0
    MATERIAL_SINGLE_VALUE_PER_CHUNK = 1
    MATERIAL_ONE_BYTE_PER_TRIANGLE = 2
    MATERIAL_TWO_BYTES_PER_TRIANGLE = 3
    MATERIAL_FOUR_BYTES_PER_TRIANGLE = 4


class hkpCompressedMeshShape(hkpShapeCollection):
    bitsPerIndex: int
    bitsPerWIndex: int
    wIndexMask: int
    indexMask: int
    radius: float
    weldingType: WeldingType
    materialType: MaterialType
    materials: any
    materials16: any
    materials8: any
    transforms: any
    bigVertices: any
    bigTriangles: hkpCompressedMeshShapeBigTriangle
    chunks: hkpCompressedMeshShapeChunk
    convexPieces: hkpCompressedMeshShapeConvexPiece
    error: float
    bounds: hkAabb
    defaultCollisionFilterInfo: int
    meshMaterials: any
    materialStriding: int
    numMaterials: int
    namedMaterials: hkpNamedMeshMaterial

    def __init__(self, infile):
        self.bitsPerIndex = struct.unpack('>i', infile.read(4))
        self.bitsPerWIndex = struct.unpack('>i', infile.read(4))
        self.wIndexMask = struct.unpack('>i', infile.read(4))
        self.indexMask = struct.unpack('>i', infile.read(4))
        self.radius = struct.unpack('>f', infile.read(4))
        self.weldingType = WeldingType(infile)  # TYPE_ENUM
        self.materialType = MaterialType(infile)  # TYPE_ENUM
        self.materials = any(infile)  # TYPE_ARRAY
        self.materials16 = any(infile)  # TYPE_ARRAY
        self.materials8 = any(infile)  # TYPE_ARRAY
        self.transforms = any(infile)  # TYPE_ARRAY
        self.bigVertices = any(infile)  # TYPE_ARRAY
        self.bigTriangles = hkpCompressedMeshShapeBigTriangle(infile)  # TYPE_ARRAY
        self.chunks = hkpCompressedMeshShapeChunk(infile)  # TYPE_ARRAY
        self.convexPieces = hkpCompressedMeshShapeConvexPiece(infile)  # TYPE_ARRAY
        self.error = struct.unpack('>f', infile.read(4))
        self.bounds = hkAabb(infile)  # TYPE_STRUCT
        self.defaultCollisionFilterInfo = struct.unpack('>I', infile.read(4))
        self.meshMaterials = any(infile)  # TYPE_POINTER
        self.materialStriding = struct.unpack('>H', infile.read(2))
        self.numMaterials = struct.unpack('>H', infile.read(2))
        self.namedMaterials = hkpNamedMeshMaterial(infile)  # TYPE_ARRAY
