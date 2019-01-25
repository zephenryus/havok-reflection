from .hclOperator import hclOperator
from typing import List
from .common import get_array
import struct
from .hclBoneSpaceDeformer import hclBoneSpaceDeformer


class hclBoneSpaceSkinOperator(hclOperator):
    transformSubset: List[int]
    outputBufferIndex: int
    transformSetIndex: int
    boneSpaceDeformer: hclBoneSpaceDeformer

    def __init__(self, infile):
        self.transformSubset = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.outputBufferIndex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.transformSetIndex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.boneSpaceDeformer = hclBoneSpaceDeformer(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transformSubset=[{transformSubset}], outputBufferIndex={outputBufferIndex}, transformSetIndex={transformSetIndex}, boneSpaceDeformer={boneSpaceDeformer}>".format(**{
            "class_name": self.__class__.__name__,
            "transformSubset": self.transformSubset,
            "outputBufferIndex": self.outputBufferIndex,
            "transformSetIndex": self.transformSetIndex,
            "boneSpaceDeformer": self.boneSpaceDeformer,
        })
