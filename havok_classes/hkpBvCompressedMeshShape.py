from .hkpBvTreeShape import hkpBvTreeShape
from enum import Enum
import struct
from .enums import WeldingType
from .common import any
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
    collisionFilterInfoPalette: any
    userDataPalette: any
    userStringPalette: any
    tree: hkpBvCompressedMeshShapeTree

    def __init__(self, infile):
        self.convexRadius = struct.unpack('>f', infile.read(4))
        self.weldingType = WeldingType(infile)  # TYPE_ENUM
        self.hasPerPrimitiveCollisionFilterInfo = struct.unpack('>?', infile.read(1))
        self.hasPerPrimitiveUserData = struct.unpack('>?', infile.read(1))
        self.collisionFilterInfoPalette = any(infile)  # TYPE_ARRAY
        self.userDataPalette = any(infile)  # TYPE_ARRAY
        self.userStringPalette = any(infile)  # TYPE_ARRAY
        self.tree = hkpBvCompressedMeshShapeTree(infile)  # TYPE_STRUCT
