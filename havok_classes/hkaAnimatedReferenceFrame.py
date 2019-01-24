from .hkReferencedObject import hkReferencedObject
from enum import Enum


class hkaReferenceFrameTypeEnum(Enum):
    REFERENCE_FRAME_UNKNOWN = 0
    REFERENCE_FRAME_DEFAULT = 1
    REFERENCE_FRAME_PARAMETRIC = 2


class hkaAnimatedReferenceFrame(hkReferencedObject):
    frameType: enumerate
