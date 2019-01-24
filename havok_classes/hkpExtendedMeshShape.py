from .hkpShapeCollection import hkpShapeCollection
from enum import Enum
from .hkpExtendedMeshShapeTrianglesSubpart import hkpExtendedMeshShapeTrianglesSubpart
from .common import vector4, any
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
