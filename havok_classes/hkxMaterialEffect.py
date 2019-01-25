from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .enums import EffectType
from .common import any


class EffectType(Enum):
    EFFECT_TYPE_INVALID = 0
    EFFECT_TYPE_UNKNOWN = 1
    EFFECT_TYPE_HLSL_FX_INLINE = 2
    EFFECT_TYPE_CG_FX_INLINE = 3
    EFFECT_TYPE_HLSL_FX_FILENAME = 4
    EFFECT_TYPE_CG_FX_FILENAME = 5
    EFFECT_TYPE_MAX_ID = 6


class hkxMaterialEffect(hkReferencedObject):
    name: str
    type: EffectType
    data: any

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.type = EffectType(infile)  # TYPE_ENUM
        self.data = any(infile)  # TYPE_ARRAY
