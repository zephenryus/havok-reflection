from .hkpHeightFieldShape import hkpHeightFieldShape
from enum import Enum
from typing import List
from .common import get_array
from .hkpSampledHeightFieldShapeCoarseMinMaxLevel import hkpSampledHeightFieldShapeCoarseMinMaxLevel
import struct
from .enums import HeightFieldType


class HeightFieldType(Enum):
    HEIGHTFIELD_STORAGE = 0
    HEIGHTFIELD_COMPRESSED = 1
    HEIGHTFIELD_USER = 2
    HEIGHTFIELD_MAX_ID = 3


class hkpSampledHeightFieldShape(hkpHeightFieldShape):
    coarseTreeData: List[hkpSampledHeightFieldShapeCoarseMinMaxLevel]
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
        self.coarseTreeData = get_array(infile, hkpSampledHeightFieldShapeCoarseMinMaxLevel, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.coarseness = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.raycastMinY = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.raycastMaxY = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.xRes = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.zRes = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.heightCenter = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.useProjectionBasedHeight = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.heightfieldType = HeightFieldType(infile)  # TYPE_ENUM:TYPE_UINT8
        self.intToFloatScale = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.floatToIntScale = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.floatToIntOffsetFloorCorrected = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.extents = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} coarseTreeData=[{coarseTreeData}], coarseness={coarseness}, raycastMinY={raycastMinY}, raycastMaxY={raycastMaxY}, xRes={xRes}, zRes={zRes}, heightCenter={heightCenter}, useProjectionBasedHeight={useProjectionBasedHeight}, heightfieldType={heightfieldType}, intToFloatScale={intToFloatScale}, floatToIntScale={floatToIntScale}, floatToIntOffsetFloorCorrected={floatToIntOffsetFloorCorrected}, extents={extents}>".format(**{
            "class_name": self.__class__.__name__,
            "coarseTreeData": self.coarseTreeData,
            "coarseness": self.coarseness,
            "raycastMinY": self.raycastMinY,
            "raycastMaxY": self.raycastMaxY,
            "xRes": self.xRes,
            "zRes": self.zRes,
            "heightCenter": self.heightCenter,
            "useProjectionBasedHeight": self.useProjectionBasedHeight,
            "heightfieldType": self.heightfieldType,
            "intToFloatScale": self.intToFloatScale,
            "floatToIntScale": self.floatToIntScale,
            "floatToIntOffsetFloorCorrected": self.floatToIntOffsetFloorCorrected,
            "extents": self.extents,
        })
