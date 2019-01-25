from .hkpShapeCollection import hkpShapeCollection
from enum import Enum
from .hkpExtendedMeshShapeTrianglesSubpart import hkpExtendedMeshShapeTrianglesSubpart
from .common import vector4, any
import struct
from .hkpExtendedMeshShapeShapesSubpart import hkpExtendedMeshShapeShapesSubpart
from .enums import WeldingType


class IndexStridingType(Enum):
    INDICES_INVALID = 0
    INDICES_INT8 = 1
    INDICES_INT16 = 2
    INDICES_INT32 = 3
    INDICES_MAX_ID = 4


class MaterialIndexStridingType(Enum):
    MATERIAL_INDICES_INVALID = 0
    MATERIAL_INDICES_INT8 = 1
    MATERIAL_INDICES_INT16 = 2
    MATERIAL_INDICES_MAX_ID = 3


class SubpartType(Enum):
    SUBPART_TRIANGLES = 0
    SUBPART_SHAPE = 1
    SUBPART_TYPE_MAX = 2


class SubpartTypesAndFlags(Enum):
    SUBPART_TYPE_MASK = 1
    SUBPART_MATERIAL_INDICES_MASK = 6
    SUBPART_MATERIAL_INDICES_SHIFT = 1
    SUBPART_NUM_MATERIALS_MASK = 65528
    SUBPART_NUM_MATERIALS_SHIFT = 3


class hkpExtendedMeshShape(hkpShapeCollection):
    embeddedTrianglesSubpart: hkpExtendedMeshShapeTrianglesSubpart
    aabbHalfExtents: vector4
    aabbCenter: vector4
    materialClass: any
    numBitsForSubpartIndex: int
    trianglesSubparts: hkpExtendedMeshShapeTrianglesSubpart
    shapesSubparts: hkpExtendedMeshShapeShapesSubpart
    weldingInfo: any
    weldingType: WeldingType
    defaultCollisionFilterInfo: int
    cachedNumChildShapes: int
    triangleRadius: float
    padding: int

    def __init__(self, infile):
        self.embeddedTrianglesSubpart = hkpExtendedMeshShapeTrianglesSubpart(infile)  # TYPE_STRUCT
        self.aabbHalfExtents = struct.unpack('>4f', infile.read(16))
        self.aabbCenter = struct.unpack('>4f', infile.read(16))
        self.materialClass = any(infile)  # TYPE_POINTER
        self.numBitsForSubpartIndex = struct.unpack('>i', infile.read(4))
        self.trianglesSubparts = hkpExtendedMeshShapeTrianglesSubpart(infile)  # TYPE_ARRAY
        self.shapesSubparts = hkpExtendedMeshShapeShapesSubpart(infile)  # TYPE_ARRAY
        self.weldingInfo = any(infile)  # TYPE_ARRAY
        self.weldingType = WeldingType(infile)  # TYPE_ENUM
        self.defaultCollisionFilterInfo = struct.unpack('>I', infile.read(4))
        self.cachedNumChildShapes = struct.unpack('>i', infile.read(4))
        self.triangleRadius = struct.unpack('>f', infile.read(4))
        self.padding = struct.unpack('>i', infile.read(4))
