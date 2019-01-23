from .hclOperator import hclOperator
from .hclBlendSomeVerticesOperatorBlendEntry import hclBlendSomeVerticesOperatorBlendEntry


class hclBlendSomeVerticesOperator(hclOperator):
	blendEntries: hclBlendSomeVerticesOperatorBlendEntry
	bufferIdx_A: int
	bufferIdx_B: int
	bufferIdx_C: int
	blendNormals: bool
	blendTangents: bool
	blendBitangents: bool
