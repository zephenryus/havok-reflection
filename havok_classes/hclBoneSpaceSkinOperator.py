from .hclOperator import hclOperator
from .common import any
import struct
from .hclBoneSpaceDeformer import hclBoneSpaceDeformer


class hclBoneSpaceSkinOperator(hclOperator):
    transformSubset: any
    outputBufferIndex: int
    transformSetIndex: int
    boneSpaceDeformer: hclBoneSpaceDeformer

    def __init__(self, infile):
        self.transformSubset = any(infile)  # TYPE_ARRAY
        self.outputBufferIndex = struct.unpack('>I', infile.read(4))
        self.transformSetIndex = struct.unpack('>I', infile.read(4))
        self.boneSpaceDeformer = hclBoneSpaceDeformer(infile)  # TYPE_STRUCT
