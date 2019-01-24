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
