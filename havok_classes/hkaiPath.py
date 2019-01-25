from .hkReferencedObject import hkReferencedObject
from enum import Enum
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
    points: hkaiPathPathPoint
    referenceFrame: ReferenceFrame

    def __init__(self, infile):
        self.points = hkaiPathPathPoint(infile)  # TYPE_ARRAY
        self.referenceFrame = ReferenceFrame(infile)  # TYPE_ENUM
