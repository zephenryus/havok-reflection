from .hkpShapeCollection import hkpShapeCollection
from enum import Enum
from .hkpExtendedMeshShapeTrianglesSubpart import hkpExtendedMeshShapeTrianglesSubpart
import struct
from typing import List
from .common import get_array
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
    trianglesSubparts: List[hkpExtendedMeshShapeTrianglesSubpart]
    shapesSubparts: List[hkpExtendedMeshShapeShapesSubpart]
    weldingInfo: List[int]
    weldingType: WeldingType
    defaultCollisionFilterInfo: int
    cachedNumChildShapes: int
    triangleRadius: float
    padding: int

    def __init__(self, infile):
        self.embeddedTrianglesSubpart = hkpExtendedMeshShapeTrianglesSubpart(infile)  # TYPE_STRUCT:TYPE_VOID
        self.aabbHalfExtents = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.aabbCenter = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.materialClass = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.numBitsForSubpartIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.trianglesSubparts = get_array(infile, hkpExtendedMeshShapeTrianglesSubpart, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.shapesSubparts = get_array(infile, hkpExtendedMeshShapeShapesSubpart, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.weldingInfo = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.weldingType = WeldingType(infile)  # TYPE_ENUM:TYPE_UINT8
        self.defaultCollisionFilterInfo = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.cachedNumChildShapes = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.triangleRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.padding = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} embeddedTrianglesSubpart={embeddedTrianglesSubpart}, aabbHalfExtents={aabbHalfExtents}, aabbCenter={aabbCenter}, materialClass={materialClass}, numBitsForSubpartIndex={numBitsForSubpartIndex}, trianglesSubparts=[{trianglesSubparts}], shapesSubparts=[{shapesSubparts}], weldingInfo=[{weldingInfo}], weldingType={weldingType}, defaultCollisionFilterInfo={defaultCollisionFilterInfo}, cachedNumChildShapes={cachedNumChildShapes}, triangleRadius={triangleRadius}, padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "embeddedTrianglesSubpart": self.embeddedTrianglesSubpart,
            "aabbHalfExtents": self.aabbHalfExtents,
            "aabbCenter": self.aabbCenter,
            "materialClass": self.materialClass,
            "numBitsForSubpartIndex": self.numBitsForSubpartIndex,
            "trianglesSubparts": self.trianglesSubparts,
            "shapesSubparts": self.shapesSubparts,
            "weldingInfo": self.weldingInfo,
            "weldingType": self.weldingType,
            "defaultCollisionFilterInfo": self.defaultCollisionFilterInfo,
            "cachedNumChildShapes": self.cachedNumChildShapes,
            "triangleRadius": self.triangleRadius,
            "padding": self.padding,
        })
