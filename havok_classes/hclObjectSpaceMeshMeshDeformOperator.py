from .hclOperator import hclOperator
from .hclObjectSpaceDeformer import hclObjectSpaceDeformer


class hclObjectSpaceMeshMeshDeformOperator(hclOperator):
	inputBufferIdx: int
	outputBufferIdx: int
	scaleNormalBehaviour: any
	inputTrianglesSubset: any
	triangleFromMeshTransforms: any
	objectSpaceDeformer: hclObjectSpaceDeformer
	customSkinDeform: bool
