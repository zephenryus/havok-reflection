from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .common import any
from .enums import VertexFloatDimensions


class VertexFloatDimensions(Enum):
    FLOAT = 0
    DISTANCE = 1
    ANGLE = 2


class hkxVertexFloatDataChannel(hkReferencedObject):
    perVertexFloats: any
    dimensions: VertexFloatDimensions
