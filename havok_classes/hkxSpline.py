from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkxSplineControlPoint import hkxSplineControlPoint


class ControlType(Enum):
    BEZIER_SMOOTH = 0
    BEZIER_CORNER = 1
    LINEAR = 2
    CUSTOM = 3


class hkxSpline(hkReferencedObject):
    controlPoints: hkxSplineControlPoint
    isClosed: bool
