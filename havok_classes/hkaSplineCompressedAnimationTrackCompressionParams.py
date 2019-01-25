from enum import Enum
import struct
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

    def __init__(self, infile):
        self.rotationTolerance = struct.unpack('>f', infile.read(4))
        self.translationTolerance = struct.unpack('>f', infile.read(4))
        self.scaleTolerance = struct.unpack('>f', infile.read(4))
        self.floatingTolerance = struct.unpack('>f', infile.read(4))
        self.rotationDegree = struct.unpack('>H', infile.read(2))
        self.translationDegree = struct.unpack('>H', infile.read(2))
        self.scaleDegree = struct.unpack('>H', infile.read(2))
        self.floatingDegree = struct.unpack('>H', infile.read(2))
        self.rotationQuantizationType = RotationQuantization(infile)  # TYPE_ENUM
        self.translationQuantizationType = ScalarQuantization(infile)  # TYPE_ENUM
        self.scaleQuantizationType = ScalarQuantization(infile)  # TYPE_ENUM
        self.floatQuantizationType = ScalarQuantization(infile)  # TYPE_ENUM
