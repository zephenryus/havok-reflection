from .hkaAnimation import hkaAnimation
from enum import Enum
from .common import any


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
    compressedData: any
    intData: any
    intArrayOffsets: int
    floatData: any
    floatArrayOffsets: int
    numBones: int
    numFloatSlots: int
    numFrames: int
    firstFloatBlockScaleAndOffsetIndex: int
    skeleton: any
    maxCompressedBytesPerFrame: int
