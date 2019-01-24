from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .enums import LightType
from .common import vector4


class LightType(Enum):
    POINT_LIGHT = 0
    DIRECTIONAL_LIGHT = 1
    SPOT_LIGHT = 2


class hkxLight(hkReferencedObject):
    type: LightType
    position: vector4
    direction: vector4
    color: int
    angle: float
    range: float
    fadeStart: float
    fadeEnd: float
    decayRate: int
    intensity: float
    shadowCaster: bool
