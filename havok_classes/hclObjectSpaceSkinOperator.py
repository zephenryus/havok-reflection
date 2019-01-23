from .hclOperator import hclOperator
from .hclObjectSpaceDeformer import hclObjectSpaceDeformer


class hclObjectSpaceSkinOperator(hclOperator):
	boneFromSkinMeshTransforms: any
	transformSubset: any
	outputBufferIndex: int
	transformSetIndex: int
	objectSpaceDeformer: hclObjectSpaceDeformer
