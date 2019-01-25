from .hkReferencedObject import hkReferencedObject
from enum import Enum
from typing import List
from .common import get_array
from .hkxSplineControlPoint import hkxSplineControlPoint
import struct


class ControlType(Enum):
    BEZIER_SMOOTH = 0
    BEZIER_CORNER = 1
    LINEAR = 2
    CUSTOM = 3


class hkxSpline(hkReferencedObject):
    controlPoints: List[hkxSplineControlPoint]
    isClosed: bool

    def __init__(self, infile):
        self.controlPoints = get_array(infile, hkxSplineControlPoint, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.isClosed = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} controlPoints=[{controlPoints}], isClosed={isClosed}>".format(**{
            "class_name": self.__class__.__name__,
            "controlPoints": self.controlPoints,
            "isClosed": self.isClosed,
        })
