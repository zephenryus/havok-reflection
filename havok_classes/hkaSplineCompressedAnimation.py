from .hkaAnimation import hkaAnimation
import struct
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

    def __init__(self, infile):
        self.numFrames = struct.unpack('>i', infile.read(4))
        self.numBlocks = struct.unpack('>i', infile.read(4))
        self.maxFramesPerBlock = struct.unpack('>i', infile.read(4))
        self.maskAndQuantizationSize = struct.unpack('>i', infile.read(4))
        self.blockDuration = struct.unpack('>f', infile.read(4))
        self.blockInverseDuration = struct.unpack('>f', infile.read(4))
        self.frameDuration = struct.unpack('>f', infile.read(4))
        self.blockOffsets = any(infile)  # TYPE_ARRAY
        self.floatBlockOffsets = any(infile)  # TYPE_ARRAY
        self.transformOffsets = any(infile)  # TYPE_ARRAY
        self.floatOffsets = any(infile)  # TYPE_ARRAY
        self.data = any(infile)  # TYPE_ARRAY
        self.endian = struct.unpack('>i', infile.read(4))
