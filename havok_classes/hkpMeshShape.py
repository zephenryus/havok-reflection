from .hkpShapeCollection import hkpShapeCollection
from enum import Enum
from .common import vector4, any
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
