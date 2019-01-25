from .hkReferencedObject import hkReferencedObject
from enum import Enum


class hkaReferenceFrameTypeEnum(Enum):
    REFERENCE_FRAME_UNKNOWN = 0
    REFERENCE_FRAME_DEFAULT = 1
    REFERENCE_FRAME_PARAMETRIC = 2


class hkaAnimatedReferenceFrame(hkReferencedObject):
    frameType: enumerate

    def __init__(self, infile):
        self.frameType = enumerate(infile)  # TYPE_ENUM:TYPE_INT8

    def __repr__(self):
        return "<{class_name} frameType={frameType}>".format(**{
            "class_name": self.__class__.__name__,
            "frameType": self.frameType,
        })
