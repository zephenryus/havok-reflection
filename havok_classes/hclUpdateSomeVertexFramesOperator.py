from .hclOperator import hclOperator
from .hclUpdateSomeVertexFramesOperatorTriangle import hclUpdateSomeVertexFramesOperatorTriangle


class hclUpdateSomeVertexFramesOperator(hclOperator):
	involvedTriangles: hclUpdateSomeVertexFramesOperatorTriangle
	involvedVertices: any
	selectionVertexToInvolvedVertex: any
	involvedVertexToNormalID: any
	triangleFlips: any
	referenceVertices: any
	tangentEdgeCosAngle: any
	tangentEdgeSinAngle: any
	biTangentFlip: any
	bufferIdx: int
	numUniqueNormalIDs: int
	updateNormals: bool
	updateTangents: bool
	updateBiTangents: bool
