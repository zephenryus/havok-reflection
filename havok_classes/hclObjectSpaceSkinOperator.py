from .hclOperator import hclOperator
from typing import List
from .common import get_array
import struct
from .hclObjectSpaceDeformer import hclObjectSpaceDeformer


class hclObjectSpaceSkinOperator(hclOperator):
    boneFromSkinMeshTransforms: List[any]
    transformSubset: List[int]
    outputBufferIndex: int
    transformSetIndex: int
    objectSpaceDeformer: hclObjectSpaceDeformer

    def __init__(self, infile):
        self.boneFromSkinMeshTransforms = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_MATRIX4
        self.transformSubset = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.outputBufferIndex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.transformSetIndex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.objectSpaceDeformer = hclObjectSpaceDeformer(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} boneFromSkinMeshTransforms=[{boneFromSkinMeshTransforms}], transformSubset=[{transformSubset}], outputBufferIndex={outputBufferIndex}, transformSetIndex={transformSetIndex}, objectSpaceDeformer={objectSpaceDeformer}>".format(**{
            "class_name": self.__class__.__name__,
            "boneFromSkinMeshTransforms": self.boneFromSkinMeshTransforms,
            "transformSubset": self.transformSubset,
            "outputBufferIndex": self.outputBufferIndex,
            "transformSetIndex": self.transformSetIndex,
            "objectSpaceDeformer": self.objectSpaceDeformer,
        })
