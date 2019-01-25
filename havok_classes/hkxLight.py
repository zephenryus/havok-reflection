from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .enums import LightType
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
        self.type = LightType(infile)  # TYPE_ENUM:TYPE_INT8
        self.position = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.direction = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.color = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.angle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.range = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.fadeStart = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.fadeEnd = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.decayRate = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.intensity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.shadowCaster = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} type={type}, position={position}, direction={direction}, color={color}, angle={angle}, range={range}, fadeStart={fadeStart}, fadeEnd={fadeEnd}, decayRate={decayRate}, intensity={intensity}, shadowCaster={shadowCaster}>".format(**{
            "class_name": self.__class__.__name__,
            "type": self.type,
            "position": self.position,
            "direction": self.direction,
            "color": self.color,
            "angle": self.angle,
            "range": self.range,
            "fadeStart": self.fadeStart,
            "fadeEnd": self.fadeEnd,
            "decayRate": self.decayRate,
            "intensity": self.intensity,
            "shadowCaster": self.shadowCaster,
        })
