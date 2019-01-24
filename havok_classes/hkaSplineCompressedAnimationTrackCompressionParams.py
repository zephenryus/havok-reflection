from enum import Enum
from .enums import RotationQuantization, ScalarQuantization


class RotationQuantization(Enum):
    POLAR32 = 0
    THREECOMP40 = 1
    THREECOMP48 = 2
    THREECOMP24 = 3
    STRAIGHT16 = 4
    UNCOMPRESSED = 5


class ScalarQuantization(Enum):
    BITS8 = 0
    BITS16 = 1


class hkaSplineCompressedAnimationTrackCompressionParams(object):
    rotationTolerance: float
    translationTolerance: float
    scaleTolerance: float
    floatingTolerance: float
    rotationDegree: int
    translationDegree: int
    scaleDegree: int
    floatingDegree: int
    rotationQuantizationType: RotationQuantization
    translationQuantizationType: ScalarQuantization
    scaleQuantizationType: ScalarQuantization
    floatQuantizationType: ScalarQuantization
