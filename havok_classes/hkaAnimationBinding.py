from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaAnimation import hkaAnimation
from typing import List
from .common import get_array
from .enums import BlendHint


class BlendHint(Enum):
    NORMAL = 0
    ADDITIVE_DEPRECATED = 1
    ADDITIVE = 2


class hkaAnimationBinding(hkReferencedObject):
    originalSkeletonName: str
    animation: any
    transformTrackToBoneIndices: List[int]
    floatTrackToFloatSlotIndices: List[int]
    partitionIndices: List[int]
    blendHint: BlendHint

    def __init__(self, infile):
        self.originalSkeletonName = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.animation = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.transformTrackToBoneIndices = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_INT16
        self.floatTrackToFloatSlotIndices = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_INT16
        self.partitionIndices = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_INT16
        self.blendHint = BlendHint(infile)  # TYPE_ENUM:TYPE_INT8

    def __repr__(self):
        return "<{class_name} originalSkeletonName=\"{originalSkeletonName}\", animation={animation}, transformTrackToBoneIndices=[{transformTrackToBoneIndices}], floatTrackToFloatSlotIndices=[{floatTrackToFloatSlotIndices}], partitionIndices=[{partitionIndices}], blendHint={blendHint}>".format(**{
            "class_name": self.__class__.__name__,
            "originalSkeletonName": self.originalSkeletonName,
            "animation": self.animation,
            "transformTrackToBoneIndices": self.transformTrackToBoneIndices,
            "floatTrackToFloatSlotIndices": self.floatTrackToFloatSlotIndices,
            "partitionIndices": self.partitionIndices,
            "blendHint": self.blendHint,
        })
