from .hclOperator import hclOperator


class hclCopyVerticesOperator(hclOperator):
	inputBufferIdx: int
	outputBufferIdx: int
	numberOfVertices: int
	startVertexIn: int
	startVertexOut: int
	copyNormals: bool
