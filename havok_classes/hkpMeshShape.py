from .hkpShapeCollection import hkpShapeCollection
from enum import Enum
from .common import vector4, any
import struct
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
    subparts: hkpMeshShapeSubpart
    weldingInfo: any
    weldingType: WeldingType
    radius: float
    pad: int

    def __init__(self, infile):
        self.scaling = struct.unpack('>4f', infile.read(16))
        self.numBitsForSubpartIndex = struct.unpack('>i', infile.read(4))
        self.subparts = hkpMeshShapeSubpart(infile)  # TYPE_ARRAY
        self.weldingInfo = any(infile)  # TYPE_ARRAY
        self.weldingType = WeldingType(infile)  # TYPE_ENUM
        self.radius = struct.unpack('>f', infile.read(4))
        self.pad = struct.unpack('>i', infile.read(4))
