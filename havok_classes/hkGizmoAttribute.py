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
        self.visible = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.label = str(infile)  # TYPE_CSTRING:TYPE_VOID
        self.type = GizmoType(infile)  # TYPE_ENUM:TYPE_INT8

    def __repr__(self):
        return "<{class_name} visible={visible}, label=\"{label}\", type={type}>".format(**{
            "class_name": self.__class__.__name__,
            "visible": self.visible,
            "label": self.label,
            "type": self.type,
        })
