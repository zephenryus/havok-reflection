from .hkaAnimation import hkaAnimation
from .common import any


class hkaSplineCompressedAnimation(hkaAnimation):
    numFrames: int
    numBlocks: int
    maxFramesPerBlock: int
    maskAndQuantizationSize: int
    blockDuration: float
    blockInverseDuration: float
    frameDuration: float
    blockOffsets: any
    floatBlockOffsets: any
    transformOffsets: any
    floatOffsets: any
    data: any
    endian: int
