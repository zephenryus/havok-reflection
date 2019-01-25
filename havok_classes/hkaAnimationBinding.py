from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaAnimation import hkaAnimation
from .common import any
from .enums import BlendHint


class BlendHint(Enum):
    NORMAL = 0
    ADDITIVE_DEPRECATED = 1
    ADDITIVE = 2


class hkaAnimationBinding(hkReferencedObject):
    originalSkeletonName: str
    animation: hkaAnimation
    transformTrackToBoneIndices: any
    floatTrackToFloatSlotIndices: any
    partitionIndices: any
    blendHint: BlendHint

    def __init__(self, infile):
        self.originalSkeletonName = struct.unpack('>s', infile.read(0))
        self.animation = hkaAnimation(infile)  # TYPE_POINTER
        self.transformTrackToBoneIndices = any(infile)  # TYPE_ARRAY
        self.floatTrackToFloatSlotIndices = any(infile)  # TYPE_ARRAY
        self.partitionIndices = any(infile)  # TYPE_ARRAY
        self.blendHint = BlendHint(infile)  # TYPE_ENUM
