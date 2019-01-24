from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .enums import ShaderType
from .common import any


class ShaderType(Enum):
    EFFECT_TYPE_INVALID = 0
    EFFECT_TYPE_UNKNOWN = 1
    EFFECT_TYPE_HLSL_INLINE = 2
    EFFECT_TYPE_CG_INLINE = 3
    EFFECT_TYPE_HLSL_FILENAME = 4
    EFFECT_TYPE_CG_FILENAME = 5
    EFFECT_TYPE_MAX_ID = 6


class hkxMaterialShader(hkReferencedObject):
    name: str
    type: ShaderType
    vertexEntryName: str
    geomEntryName: str
    pixelEntryName: str
    data: any
