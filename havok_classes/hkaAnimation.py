from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .enums import AnimationType
from .hkaAnimatedReferenceFrame import hkaAnimatedReferenceFrame
from .hkaAnnotationTrack import hkaAnnotationTrack


class AnimationType(Enum):
    HK_UNKNOWN_ANIMATION = 0
    HK_INTERLEAVED_ANIMATION = 1
    HK_MIRRORED_ANIMATION = 2
    HK_SPLINE_COMPRESSED_ANIMATION = 3
    HK_QUANTIZED_COMPRESSED_ANIMATION = 4
    HK_PREDICTIVE_COMPRESSED_ANIMATION = 5
    HK_REFERENCE_POSE_ANIMATION = 6


class hkaAnimation(hkReferencedObject):
    type: AnimationType
    duration: float
    numberOfTransformTracks: int
    numberOfFloatTracks: int
    extractedMotion: hkaAnimatedReferenceFrame
    annotationTracks: hkaAnnotationTrack
