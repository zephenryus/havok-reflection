from .hkpShapeCollection import hkpShapeCollection
from enum import Enum
import struct
from typing import List
from .common import get_array
from .hkpMeshShapeSubpart import hkpMeshShapeSubpart
from .enums import WeldingType


class MeshShapeIndexStridingType(Enum):
    INDICES_INVALID = 0
    INDICES_INT16 = 1
    INDICES_INT32 = 2
    INDICES_MAX_ID = 3


class MeshShapeMaterialIndexStridingType(Enum):
    MATERIAL_INDICES_INVALID = 0
    MATERIAL_INDICES_INT8 = 1
    MATERIAL_INDICES_INT16 = 2
    MATERIAL_INDICES_MAX_ID = 3


class hkpMeshShape(hkpShapeCollection):
    scaling: vector4
    numBitsForSubpartIndex: int
    subparts: List[hkpMeshShapeSubpart]
    weldingInfo: List[int]
    weldingType: WeldingType
    radius: float
    pad: int

    def __init__(self, infile):
        self.scaling = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.numBitsForSubpartIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.subparts = get_array(infile, hkpMeshShapeSubpart, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.weldingInfo = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.weldingType = WeldingType(infile)  # TYPE_ENUM:TYPE_UINT8
        self.radius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.pad = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} scaling={scaling}, numBitsForSubpartIndex={numBitsForSubpartIndex}, subparts=[{subparts}], weldingInfo=[{weldingInfo}], weldingType={weldingType}, radius={radius}, pad={pad}>".format(**{
            "class_name": self.__class__.__name__,
            "scaling": self.scaling,
            "numBitsForSubpartIndex": self.numBitsForSubpartIndex,
            "subparts": self.subparts,
            "weldingInfo": self.weldingInfo,
            "weldingType": self.weldingType,
            "radius": self.radius,
            "pad": self.pad,
        })
