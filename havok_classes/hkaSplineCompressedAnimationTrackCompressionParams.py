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
        self.rotationTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.translationTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.scaleTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.floatingTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.rotationDegree = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.translationDegree = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.scaleDegree = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.floatingDegree = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.rotationQuantizationType = RotationQuantization(infile)  # TYPE_ENUM:TYPE_UINT8
        self.translationQuantizationType = ScalarQuantization(infile)  # TYPE_ENUM:TYPE_UINT8
        self.scaleQuantizationType = ScalarQuantization(infile)  # TYPE_ENUM:TYPE_UINT8
        self.floatQuantizationType = ScalarQuantization(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} rotationTolerance={rotationTolerance}, translationTolerance={translationTolerance}, scaleTolerance={scaleTolerance}, floatingTolerance={floatingTolerance}, rotationDegree={rotationDegree}, translationDegree={translationDegree}, scaleDegree={scaleDegree}, floatingDegree={floatingDegree}, rotationQuantizationType={rotationQuantizationType}, translationQuantizationType={translationQuantizationType}, scaleQuantizationType={scaleQuantizationType}, floatQuantizationType={floatQuantizationType}>".format(**{
            "class_name": self.__class__.__name__,
            "rotationTolerance": self.rotationTolerance,
            "translationTolerance": self.translationTolerance,
            "scaleTolerance": self.scaleTolerance,
            "floatingTolerance": self.floatingTolerance,
            "rotationDegree": self.rotationDegree,
            "translationDegree": self.translationDegree,
            "scaleDegree": self.scaleDegree,
            "floatingDegree": self.floatingDegree,
            "rotationQuantizationType": self.rotationQuantizationType,
            "translationQuantizationType": self.translationQuantizationType,
            "scaleQuantizationType": self.scaleQuantizationType,
            "floatQuantizationType": self.floatQuantizationType,
        })
