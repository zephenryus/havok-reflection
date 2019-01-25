from .hclOperator import hclOperator
from .common import any
import struct
from .hclObjectSpaceDeformer import hclObjectSpaceDeformer


class hclObjectSpaceSkinOperator(hclOperator):
    boneFromSkinMeshTransforms: any
    transformSubset: any
    outputBufferIndex: int
    transformSetIndex: int
    objectSpaceDeformer: hclObjectSpaceDeformer

    def __init__(self, infile):
        self.boneFromSkinMeshTransforms = any(infile)  # TYPE_ARRAY
        self.transformSubset = any(infile)  # TYPE_ARRAY
        self.outputBufferIndex = struct.unpack('>I', infile.read(4))
        self.transformSetIndex = struct.unpack('>I', infile.read(4))
        self.objectSpaceDeformer = hclObjectSpaceDeformer(infile)  # TYPE_STRUCT
