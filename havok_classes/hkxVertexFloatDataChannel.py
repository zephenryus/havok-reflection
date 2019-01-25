from .hkReferencedObject import hkReferencedObject
from enum import Enum
from typing import List
from .common import get_array
from .enums import VertexFloatDimensions


class VertexFloatDimensions(Enum):
    FLOAT = 0
    DISTANCE = 1
    ANGLE = 2


class hkxVertexFloatDataChannel(hkReferencedObject):
    perVertexFloats: List[float]
    dimensions: VertexFloatDimensions

    def __init__(self, infile):
        self.perVertexFloats = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.dimensions = VertexFloatDimensions(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} perVertexFloats=[{perVertexFloats}], dimensions={dimensions}>".format(**{
            "class_name": self.__class__.__name__,
            "perVertexFloats": self.perVertexFloats,
            "dimensions": self.dimensions,
        })
