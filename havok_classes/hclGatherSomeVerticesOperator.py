from .hclOperator import hclOperator
from .hclGatherSomeVerticesOperatorVertexPair import hclGatherSomeVerticesOperatorVertexPair


class hclGatherSomeVerticesOperator(hclOperator):
	vertexPairs: hclGatherSomeVerticesOperatorVertexPair
	inputBufferIdx: int
	outputBufferIdx: int
	gatherNormals: bool
