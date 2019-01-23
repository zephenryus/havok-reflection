from .hclOperator import hclOperator
from .hclBoneSpaceDeformer import hclBoneSpaceDeformer


class hclBoneSpaceSkinOperator(hclOperator):
	transformSubset: any
	outputBufferIndex: int
	transformSetIndex: int
	boneSpaceDeformer: hclBoneSpaceDeformer
