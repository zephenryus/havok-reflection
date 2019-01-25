from .hkaAnimation import hkaAnimation
from enum import Enum
from typing import List
from .common import get_array
import struct


class StorageClass(Enum):
    STORAGE_STATIC = 0
    STORAGE_REFERENCE = 1
    STORAGE_DYNAMIC_RANGE = 2
    STORAGE_DYNAMIC_FIXED = 3


class IntArrayID(Enum):
    BLOCK_OFFSETS = 0
    FIRST_FLOAT_BLOCK_OFFSETS = 1
    IS_ANIMATED_BITMAP = 2
    IS_FIXED_RANGE_BITMAP = 3
    DYNAMIC_BONE_TRACK_INDEX = 4
    DYNAMIC_FLOAT_TRACK_INDEX = 5
    STATIC_BONE_TRACK_INDEX = 6
    STATIC_FLOAT_TRACK_INDEX = 7
    RENORM_QUATERNION_INDEX = 8
    NUM_INT_ARRAYS = 9


class FloatArrayID(Enum):
    STATIC_VALUES = 0
    DYNAMIC_SCALES = 1
    DYNAMIC_OFFSETS = 2
    NUM_FLOAT_ARRAYS = 3


class hkaPredictiveCompressedAnimation(hkaAnimation):
    compressedData: List[int]
    intData: List[int]
    intArrayOffsets: int
    floatData: List[float]
    floatArrayOffsets: int
    numBones: int
    numFloatSlots: int
    numFrames: int
    firstFloatBlockScaleAndOffsetIndex: int
    skeleton: any
    maxCompressedBytesPerFrame: int

    def __init__(self, infile):
        self.compressedData = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.intData = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.intArrayOffsets = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.floatData = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.floatArrayOffsets = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numBones = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numFloatSlots = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numFrames = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.firstFloatBlockScaleAndOffsetIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.skeleton = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.maxCompressedBytesPerFrame = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} compressedData=[{compressedData}], intData=[{intData}], intArrayOffsets={intArrayOffsets}, floatData=[{floatData}], floatArrayOffsets={floatArrayOffsets}, numBones={numBones}, numFloatSlots={numFloatSlots}, numFrames={numFrames}, firstFloatBlockScaleAndOffsetIndex={firstFloatBlockScaleAndOffsetIndex}, skeleton={skeleton}, maxCompressedBytesPerFrame={maxCompressedBytesPerFrame}>".format(**{
            "class_name": self.__class__.__name__,
            "compressedData": self.compressedData,
            "intData": self.intData,
            "intArrayOffsets": self.intArrayOffsets,
            "floatData": self.floatData,
            "floatArrayOffsets": self.floatArrayOffsets,
            "numBones": self.numBones,
            "numFloatSlots": self.numFloatSlots,
            "numFrames": self.numFrames,
            "firstFloatBlockScaleAndOffsetIndex": self.firstFloatBlockScaleAndOffsetIndex,
            "skeleton": self.skeleton,
            "maxCompressedBytesPerFrame": self.maxCompressedBytesPerFrame,
        })
