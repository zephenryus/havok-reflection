from .hclOperator import hclOperator
from enum import Enum
from typing import List
from .common import get_array
from .hclBlendSomeVerticesOperatorBlendEntry import hclBlendSomeVerticesOperatorBlendEntry
import struct


class VectorContext(Enum):
    VEC_POSITION = 0
    VEC_DIRECTION = 1


class hclBlendSomeVerticesOperator(hclOperator):
    blendEntries: List[hclBlendSomeVerticesOperatorBlendEntry]
    bufferIdx_A: int
    bufferIdx_B: int
    bufferIdx_C: int
    blendNormals: bool
    blendTangents: bool
    blendBitangents: bool

    def __init__(self, infile):
        self.blendEntries = get_array(infile, hclBlendSomeVerticesOperatorBlendEntry, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.bufferIdx_A = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.bufferIdx_B = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.bufferIdx_C = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.blendNormals = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.blendTangents = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.blendBitangents = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} blendEntries=[{blendEntries}], bufferIdx_A={bufferIdx_A}, bufferIdx_B={bufferIdx_B}, bufferIdx_C={bufferIdx_C}, blendNormals={blendNormals}, blendTangents={blendTangents}, blendBitangents={blendBitangents}>".format(**{
            "class_name": self.__class__.__name__,
            "blendEntries": self.blendEntries,
            "bufferIdx_A": self.bufferIdx_A,
            "bufferIdx_B": self.bufferIdx_B,
            "bufferIdx_C": self.bufferIdx_C,
            "blendNormals": self.blendNormals,
            "blendTangents": self.blendTangents,
            "blendBitangents": self.blendBitangents,
        })
