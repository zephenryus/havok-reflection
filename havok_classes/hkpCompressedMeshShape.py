from .hkpShapeCollection import hkpShapeCollection
from enum import Enum
import struct
from .enums import WeldingType, MaterialType
from typing import List
from .common import get_array
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
    materials: List[int]
    materials16: List[int]
    materials8: List[int]
    transforms: List[any]
    bigVertices: List[vector4]
    bigTriangles: List[hkpCompressedMeshShapeBigTriangle]
    chunks: List[hkpCompressedMeshShapeChunk]
    convexPieces: List[hkpCompressedMeshShapeConvexPiece]
    error: float
    bounds: hkAabb
    defaultCollisionFilterInfo: int
    meshMaterials: any
    materialStriding: int
    numMaterials: int
    namedMaterials: List[hkpNamedMeshMaterial]

    def __init__(self, infile):
        self.bitsPerIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.bitsPerWIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.wIndexMask = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.indexMask = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.radius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.weldingType = WeldingType(infile)  # TYPE_ENUM:TYPE_UINT8
        self.materialType = MaterialType(infile)  # TYPE_ENUM:TYPE_UINT8
        self.materials = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.materials16 = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.materials8 = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.transforms = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_QSTRANSFORM
        self.bigVertices = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.bigTriangles = get_array(infile, hkpCompressedMeshShapeBigTriangle, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.chunks = get_array(infile, hkpCompressedMeshShapeChunk, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.convexPieces = get_array(infile, hkpCompressedMeshShapeConvexPiece, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.error = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.bounds = hkAabb(infile)  # TYPE_STRUCT:TYPE_VOID
        self.defaultCollisionFilterInfo = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.meshMaterials = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.materialStriding = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.numMaterials = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.namedMaterials = get_array(infile, hkpNamedMeshMaterial, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} bitsPerIndex={bitsPerIndex}, bitsPerWIndex={bitsPerWIndex}, wIndexMask={wIndexMask}, indexMask={indexMask}, radius={radius}, weldingType={weldingType}, materialType={materialType}, materials=[{materials}], materials16=[{materials16}], materials8=[{materials8}], transforms=[{transforms}], bigVertices=[{bigVertices}], bigTriangles=[{bigTriangles}], chunks=[{chunks}], convexPieces=[{convexPieces}], error={error}, bounds={bounds}, defaultCollisionFilterInfo={defaultCollisionFilterInfo}, meshMaterials={meshMaterials}, materialStriding={materialStriding}, numMaterials={numMaterials}, namedMaterials=[{namedMaterials}]>".format(**{
            "class_name": self.__class__.__name__,
            "bitsPerIndex": self.bitsPerIndex,
            "bitsPerWIndex": self.bitsPerWIndex,
            "wIndexMask": self.wIndexMask,
            "indexMask": self.indexMask,
            "radius": self.radius,
            "weldingType": self.weldingType,
            "materialType": self.materialType,
            "materials": self.materials,
            "materials16": self.materials16,
            "materials8": self.materials8,
            "transforms": self.transforms,
            "bigVertices": self.bigVertices,
            "bigTriangles": self.bigTriangles,
            "chunks": self.chunks,
            "convexPieces": self.convexPieces,
            "error": self.error,
            "bounds": self.bounds,
            "defaultCollisionFilterInfo": self.defaultCollisionFilterInfo,
            "meshMaterials": self.meshMaterials,
            "materialStriding": self.materialStriding,
            "numMaterials": self.numMaterials,
            "namedMaterials": self.namedMaterials,
        })
