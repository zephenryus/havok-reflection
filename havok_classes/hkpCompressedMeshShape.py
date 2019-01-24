from .hkpShapeCollection import hkpShapeCollection
from enum import Enum
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
