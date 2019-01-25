from .hkpBvTreeShape import hkpBvTreeShape
from enum import Enum
import struct
from .enums import WeldingType
from typing import List
from .common import get_array
from .hkpBvCompressedMeshShapeTree import hkpBvCompressedMeshShapeTree


class PerPrimitiveDataMode(Enum):
    PER_PRIMITIVE_DATA_NONE = 0
    PER_PRIMITIVE_DATA_8_BIT = 1
    PER_PRIMITIVE_DATA_PALETTE = 2
    PER_PRIMITIVE_DATA_STRING_PALETTE = 3


class PrimitiveType(Enum):
    PRIMITIVE_TYPE_BOX = 0
    PRIMITIVE_TYPE_HULL = 1
    PRIMITIVE_TYPE_SPHERE = 2
    PRIMITIVE_TYPE_CAPSULE = 3
    PRIMITIVE_TYPE_CYLINDER = 4


class Config(Enum):
    NUM_BYTES_FOR_TREE = 144
    MAX_NUM_VERTICES_PER_HULL = 255
    MAX_NUM_PRIMITIVES = 8388608


class hkpBvCompressedMeshShape(hkpBvTreeShape):
    convexRadius: float
    weldingType: WeldingType
    hasPerPrimitiveCollisionFilterInfo: bool
    hasPerPrimitiveUserData: bool
    collisionFilterInfoPalette: List[int]
    userDataPalette: List[int]
    userStringPalette: List[str]
    tree: hkpBvCompressedMeshShapeTree

    def __init__(self, infile):
        self.convexRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.weldingType = WeldingType(infile)  # TYPE_ENUM:TYPE_UINT8
        self.hasPerPrimitiveCollisionFilterInfo = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.hasPerPrimitiveUserData = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.collisionFilterInfoPalette = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.userDataPalette = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.userStringPalette = get_array(infile, str, 0)  # TYPE_ARRAY:TYPE_STRINGPTR
        self.tree = hkpBvCompressedMeshShapeTree(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} convexRadius={convexRadius}, weldingType={weldingType}, hasPerPrimitiveCollisionFilterInfo={hasPerPrimitiveCollisionFilterInfo}, hasPerPrimitiveUserData={hasPerPrimitiveUserData}, collisionFilterInfoPalette=[{collisionFilterInfoPalette}], userDataPalette=[{userDataPalette}], userStringPalette=[{userStringPalette}], tree={tree}>".format(**{
            "class_name": self.__class__.__name__,
            "convexRadius": self.convexRadius,
            "weldingType": self.weldingType,
            "hasPerPrimitiveCollisionFilterInfo": self.hasPerPrimitiveCollisionFilterInfo,
            "hasPerPrimitiveUserData": self.hasPerPrimitiveUserData,
            "collisionFilterInfoPalette": self.collisionFilterInfoPalette,
            "userDataPalette": self.userDataPalette,
            "userStringPalette": self.userStringPalette,
            "tree": self.tree,
        })
