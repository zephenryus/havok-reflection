from .hclOperator import hclOperator
from enum import Enum
from .hclBlendSomeVerticesOperatorBlendEntry import hclBlendSomeVerticesOperatorBlendEntry
import struct


class VectorContext(Enum):
    VEC_POSITION = 0
    VEC_DIRECTION = 1


class hclBlendSomeVerticesOperator(hclOperator):
    blendEntries: hclBlendSomeVerticesOperatorBlendEntry
    bufferIdx_A: int
    bufferIdx_B: int
    bufferIdx_C: int
    blendNormals: bool
    blendTangents: bool
    blendBitangents: bool

    def __init__(self, infile):
        self.blendEntries = hclBlendSomeVerticesOperatorBlendEntry(infile)  # TYPE_ARRAY
        self.bufferIdx_A = struct.unpack('>I', infile.read(4))
        self.bufferIdx_B = struct.unpack('>I', infile.read(4))
        self.bufferIdx_C = struct.unpack('>I', infile.read(4))
        self.blendNormals = struct.unpack('>?', infile.read(1))
        self.blendTangents = struct.unpack('>?', infile.read(1))
        self.blendBitangents = struct.unpack('>?', infile.read(1))
