from .hclOperator import hclOperator


class hclGatherAllVerticesOperator(hclOperator):
	vertexInputFromVertexOutput: any
	inputBufferIdx: int
	outputBufferIdx: int
	gatherNormals: bool
	partialGather: bool
