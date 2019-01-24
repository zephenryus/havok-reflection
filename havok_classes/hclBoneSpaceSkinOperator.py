from .hclOperator import hclOperator
from .common import any
from .hclBoneSpaceDeformer import hclBoneSpaceDeformer


class hclBoneSpaceSkinOperator(hclOperator):
    transformSubset: any
    outputBufferIndex: int
    transformSetIndex: int
    boneSpaceDeformer: hclBoneSpaceDeformer
