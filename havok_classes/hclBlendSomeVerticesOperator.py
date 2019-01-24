from .hclOperator import hclOperator
from enum import Enum
from .hclBlendSomeVerticesOperatorBlendEntry import hclBlendSomeVerticesOperatorBlendEntry


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
