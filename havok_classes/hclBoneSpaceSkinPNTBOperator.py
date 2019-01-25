from .hclBoneSpaceSkinOperator import hclBoneSpaceSkinOperator
from typing import List
from .common import get_array
from .hclBoneSpaceDeformerLocalBlockPNTB import hclBoneSpaceDeformerLocalBlockPNTB
from .hclBoneSpaceDeformerLocalBlockUnpackedPNTB import hclBoneSpaceDeformerLocalBlockUnpackedPNTB


class hclBoneSpaceSkinPNTBOperator(hclBoneSpaceSkinOperator):
    localPNTBs: List[hclBoneSpaceDeformerLocalBlockPNTB]
    localUnpackedPNTBs: List[hclBoneSpaceDeformerLocalBlockUnpackedPNTB]

    def __init__(self, infile):
        self.localPNTBs = get_array(infile, hclBoneSpaceDeformerLocalBlockPNTB, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.localUnpackedPNTBs = get_array(infile, hclBoneSpaceDeformerLocalBlockUnpackedPNTB, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} localPNTBs=[{localPNTBs}], localUnpackedPNTBs=[{localUnpackedPNTBs}]>".format(**{
            "class_name": self.__class__.__name__,
            "localPNTBs": self.localPNTBs,
            "localUnpackedPNTBs": self.localUnpackedPNTBs,
        })
