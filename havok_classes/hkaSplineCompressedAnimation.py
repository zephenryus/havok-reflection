from .hkaAnimation import hkaAnimation
import struct
from typing import List
from .common import get_array


class hkaSplineCompressedAnimation(hkaAnimation):
    numFrames: int
    numBlocks: int
    maxFramesPerBlock: int
    maskAndQuantizationSize: int
    blockDuration: float
    blockInverseDuration: float
    frameDuration: float
    blockOffsets: List[int]
    floatBlockOffsets: List[int]
    transformOffsets: List[int]
    floatOffsets: List[int]
    data: List[int]
    endian: int

    def __init__(self, infile):
        self.numFrames = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numBlocks = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.maxFramesPerBlock = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.maskAndQuantizationSize = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.blockDuration = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.blockInverseDuration = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.frameDuration = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.blockOffsets = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.floatBlockOffsets = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.transformOffsets = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.floatOffsets = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.data = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.endian = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} numFrames={numFrames}, numBlocks={numBlocks}, maxFramesPerBlock={maxFramesPerBlock}, maskAndQuantizationSize={maskAndQuantizationSize}, blockDuration={blockDuration}, blockInverseDuration={blockInverseDuration}, frameDuration={frameDuration}, blockOffsets=[{blockOffsets}], floatBlockOffsets=[{floatBlockOffsets}], transformOffsets=[{transformOffsets}], floatOffsets=[{floatOffsets}], data=[{data}], endian={endian}>".format(**{
            "class_name": self.__class__.__name__,
            "numFrames": self.numFrames,
            "numBlocks": self.numBlocks,
            "maxFramesPerBlock": self.maxFramesPerBlock,
            "maskAndQuantizationSize": self.maskAndQuantizationSize,
            "blockDuration": self.blockDuration,
            "blockInverseDuration": self.blockInverseDuration,
            "frameDuration": self.frameDuration,
            "blockOffsets": self.blockOffsets,
            "floatBlockOffsets": self.floatBlockOffsets,
            "transformOffsets": self.transformOffsets,
            "floatOffsets": self.floatOffsets,
            "data": self.data,
            "endian": self.endian,
        })
