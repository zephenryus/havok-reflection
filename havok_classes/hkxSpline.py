from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkxSplineControlPoint import hkxSplineControlPoint
import struct


class ControlType(Enum):
    BEZIER_SMOOTH = 0
    BEZIER_CORNER = 1
    LINEAR = 2
    CUSTOM = 3


class hkxSpline(hkReferencedObject):
    controlPoints: hkxSplineControlPoint
    isClosed: bool

    def __init__(self, infile):
        self.controlPoints = hkxSplineControlPoint(infile)  # TYPE_ARRAY
        self.isClosed = struct.unpack('>?', infile.read(1))
