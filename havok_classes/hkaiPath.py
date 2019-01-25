from .hkReferencedObject import hkReferencedObject
from enum import Enum
from typing import List
from .common import get_array
from .hkaiPathPathPoint import hkaiPathPathPoint
from .enums import ReferenceFrame


class PathPointBits(Enum):
    EDGE_TYPE_USER_START = 1
    EDGE_TYPE_USER_END = 2
    EDGE_TYPE_SEGMENT_START = 4
    EDGE_TYPE_SEGMENT_END = 8


class ReferenceFrame(Enum):
    REFERENCE_FRAME_WORLD = 0
    REFERENCE_FRAME_SECTION_LOCAL = 1
    REFERENCE_FRAME_SECTION_FIXED = 2


class hkaiPath(hkReferencedObject):
    points: List[hkaiPathPathPoint]
    referenceFrame: ReferenceFrame

    def __init__(self, infile):
        self.points = get_array(infile, hkaiPathPathPoint, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.referenceFrame = ReferenceFrame(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} points=[{points}], referenceFrame={referenceFrame}>".format(**{
            "class_name": self.__class__.__name__,
            "points": self.points,
            "referenceFrame": self.referenceFrame,
        })
