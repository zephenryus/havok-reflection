from enum import Enum
from .enums import GizmoType


class GizmoType(Enum):
    POINT = 0
    SPHERE = 1
    PLANE = 2
    ARROW = 3


class hkGizmoAttribute(object):
    visible: bool
    label: str
    type: GizmoType
