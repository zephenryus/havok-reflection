from .hclOperator import hclOperator
from .hclMeshMeshDeformOperatorTriangleVertexPair import hclMeshMeshDeformOperatorTriangleVertexPair


class hclMeshMeshDeformOperator(hclOperator):
	inputTrianglesSubset: any
	triangleVertexPairs: hclMeshMeshDeformOperatorTriangleVertexPair
	triangleVertexStartForVertex: any
	inputBufferIdx: int
	outputBufferIdx: int
	startVertex: int
	endVertex: int
	scaleNormalBehaviour: any
	deformNormals: bool
	partialDeform: bool
