from .hclObjectSpaceSkinOperator import hclObjectSpaceSkinOperator
from typing import List
from .common import get_array
from .hclObjectSpaceDeformerLocalBlockPNTB import hclObjectSpaceDeformerLocalBlockPNTB
from .hclObjectSpaceDeformerLocalBlockUnpackedPNTB import hclObjectSpaceDeformerLocalBlockUnpackedPNTB


class hclObjectSpaceSkinPNTBOperator(hclObjectSpaceSkinOperator):
    localPNTBs: List[hclObjectSpaceDeformerLocalBlockPNTB]
    localUnpackedPNTBs: List[hclObjectSpaceDeformerLocalBlockUnpackedPNTB]

    def __init__(self, infile):
        self.localPNTBs = get_array(infile, hclObjectSpaceDeformerLocalBlockPNTB, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.localUnpackedPNTBs = get_array(infile, hclObjectSpaceDeformerLocalBlockUnpackedPNTB, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} localPNTBs=[{localPNTBs}], localUnpackedPNTBs=[{localUnpackedPNTBs}]>".format(**{
            "class_name": self.__class__.__name__,
            "localPNTBs": self.localPNTBs,
            "localUnpackedPNTBs": self.localUnpackedPNTBs,
        })
