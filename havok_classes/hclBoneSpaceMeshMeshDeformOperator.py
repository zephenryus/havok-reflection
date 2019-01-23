from .hclOperator import hclOperator
from .hclBoneSpaceDeformer import hclBoneSpaceDeformer


class hclBoneSpaceMeshMeshDeformOperator(hclOperator):
	inputBufferIdx: int
	outputBufferIdx: int
	scaleNormalBehaviour: any
	inputTrianglesSubset: any
	boneSpaceDeformer: hclBoneSpaceDeformer
