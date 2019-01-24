from .hclOperator import hclOperator
from .common import any


class hclGatherAllVerticesOperator(hclOperator):
    vertexInputFromVertexOutput: any
    inputBufferIdx: int
    outputBufferIdx: int
    gatherNormals: bool
    partialGather: bool
