from enum import Enum
import struct
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

    def __init__(self, infile):
        self.visible = struct.unpack('>?', infile.read(1))
        self.label = str(infile)  # TYPE_CSTRING
        self.type = GizmoType(infile)  # TYPE_ENUM
