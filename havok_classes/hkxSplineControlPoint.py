from .common import vector4
from .enums import ControlType


class hkxSplineControlPoint(object):
    position: vector4
    tangentIn: vector4
    tangentOut: vector4
    inType: ControlType
    outType: ControlType
