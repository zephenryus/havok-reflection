from .hclObjectSpaceSkinOperator import hclObjectSpaceSkinOperator
from typing import List
from .common import get_array
from .hclObjectSpaceDeformerLocalBlockPNT import hclObjectSpaceDeformerLocalBlockPNT
from .hclObjectSpaceDeformerLocalBlockUnpackedPNT import hclObjectSpaceDeformerLocalBlockUnpackedPNT


class hclObjectSpaceSkinPNTOperator(hclObjectSpaceSkinOperator):
    localPNTs: List[hclObjectSpaceDeformerLocalBlockPNT]
    localUnpackedPNTs: List[hclObjectSpaceDeformerLocalBlockUnpackedPNT]

    def __init__(self, infile):
        self.localPNTs = get_array(infile, hclObjectSpaceDeformerLocalBlockPNT, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.localUnpackedPNTs = get_array(infile, hclObjectSpaceDeformerLocalBlockUnpackedPNT, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} localPNTs=[{localPNTs}], localUnpackedPNTs=[{localUnpackedPNTs}]>".format(**{
            "class_name": self.__class__.__name__,
            "localPNTs": self.localPNTs,
            "localUnpackedPNTs": self.localUnpackedPNTs,
        })
