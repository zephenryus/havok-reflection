from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .enums import LightType
from .common import vector4
import struct


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

    def __init__(self, infile):
        self.type = LightType(infile)  # TYPE_ENUM
        self.position = struct.unpack('>4f', infile.read(16))
        self.direction = struct.unpack('>4f', infile.read(16))
        self.color = struct.unpack('>I', infile.read(4))
        self.angle = struct.unpack('>f', infile.read(4))
        self.range = struct.unpack('>f', infile.read(4))
        self.fadeStart = struct.unpack('>f', infile.read(4))
        self.fadeEnd = struct.unpack('>f', infile.read(4))
        self.decayRate = struct.unpack('>h', infile.read(2))
        self.intensity = struct.unpack('>f', infile.read(4))
        self.shadowCaster = struct.unpack('>?', infile.read(1))
