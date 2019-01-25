from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .enums import AnimationType
import struct
from .hkaAnimatedReferenceFrame import hkaAnimatedReferenceFrame
from typing import List
from .common import get_array
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
    extractedMotion: any
    annotationTracks: List[hkaAnnotationTrack]

    def __init__(self, infile):
        self.type = AnimationType(infile)  # TYPE_ENUM:TYPE_INT32
        self.duration = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.numberOfTransformTracks = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numberOfFloatTracks = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.extractedMotion = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.annotationTracks = get_array(infile, hkaAnnotationTrack, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} type={type}, duration={duration}, numberOfTransformTracks={numberOfTransformTracks}, numberOfFloatTracks={numberOfFloatTracks}, extractedMotion={extractedMotion}, annotationTracks=[{annotationTracks}]>".format(**{
            "class_name": self.__class__.__name__,
            "type": self.type,
            "duration": self.duration,
            "numberOfTransformTracks": self.numberOfTransformTracks,
            "numberOfFloatTracks": self.numberOfFloatTracks,
            "extractedMotion": self.extractedMotion,
            "annotationTracks": self.annotationTracks,
        })
