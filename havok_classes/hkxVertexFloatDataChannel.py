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

    def __init__(self, infile):
        self.perVertexFloats = any(infile)  # TYPE_ARRAY
        self.dimensions = VertexFloatDimensions(infile)  # TYPE_ENUM
