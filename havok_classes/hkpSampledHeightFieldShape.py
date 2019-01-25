from .hkpHeightFieldShape import hkpHeightFieldShape
from enum import Enum
from .hkpSampledHeightFieldShapeCoarseMinMaxLevel import hkpSampledHeightFieldShapeCoarseMinMaxLevel
import struct
from .enums import HeightFieldType
from .common import vector4


class HeightFieldType(Enum):
    HEIGHTFIELD_STORAGE = 0
    HEIGHTFIELD_COMPRESSED = 1
    HEIGHTFIELD_USER = 2
    HEIGHTFIELD_MAX_ID = 3


class hkpSampledHeightFieldShape(hkpHeightFieldShape):
    coarseTreeData: hkpSampledHeightFieldShapeCoarseMinMaxLevel
    coarseness: int
    raycastMinY: float
    raycastMaxY: float
    xRes: int
    zRes: int
    heightCenter: float
    useProjectionBasedHeight: bool
    heightfieldType: HeightFieldType
    intToFloatScale: vector4
    floatToIntScale: vector4
    floatToIntOffsetFloorCorrected: vector4
    extents: vector4

    def __init__(self, infile):
        self.coarseTreeData = hkpSampledHeightFieldShapeCoarseMinMaxLevel(infile)  # TYPE_ARRAY
        self.coarseness = struct.unpack('>i', infile.read(4))
        self.raycastMinY = struct.unpack('>f', infile.read(4))
        self.raycastMaxY = struct.unpack('>f', infile.read(4))
        self.xRes = struct.unpack('>i', infile.read(4))
        self.zRes = struct.unpack('>i', infile.read(4))
        self.heightCenter = struct.unpack('>f', infile.read(4))
        self.useProjectionBasedHeight = struct.unpack('>?', infile.read(1))
        self.heightfieldType = HeightFieldType(infile)  # TYPE_ENUM
        self.intToFloatScale = struct.unpack('>4f', infile.read(16))
        self.floatToIntScale = struct.unpack('>4f', infile.read(16))
        self.floatToIntOffsetFloorCorrected = struct.unpack('>4f', infile.read(16))
        self.extents = struct.unpack('>4f', infile.read(16))
