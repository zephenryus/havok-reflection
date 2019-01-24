from .hkpHeightFieldShape import hkpHeightFieldShape
from enum import Enum
from .hkpSampledHeightFieldShapeCoarseMinMaxLevel import hkpSampledHeightFieldShapeCoarseMinMaxLevel
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
