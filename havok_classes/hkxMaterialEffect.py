from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .enums import EffectType
from typing import List
from .common import get_array


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
    data: List[int]

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.type = EffectType(infile)  # TYPE_ENUM:TYPE_UINT8
        self.data = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} name=\"{name}\", type={type}, data=[{data}]>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "type": self.type,
            "data": self.data,
        })
