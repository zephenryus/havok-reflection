from .hclBoneSpaceSkinOperator import hclBoneSpaceSkinOperator
from typing import List
from .common import get_array
from .hclBoneSpaceDeformerLocalBlockPNT import hclBoneSpaceDeformerLocalBlockPNT
from .hclBoneSpaceDeformerLocalBlockUnpackedPNT import hclBoneSpaceDeformerLocalBlockUnpackedPNT


class hclBoneSpaceSkinPNTOperator(hclBoneSpaceSkinOperator):
    localPNTs: List[hclBoneSpaceDeformerLocalBlockPNT]
    localUnpackedPNTs: List[hclBoneSpaceDeformerLocalBlockUnpackedPNT]

    def __init__(self, infile):
        self.localPNTs = get_array(infile, hclBoneSpaceDeformerLocalBlockPNT, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.localUnpackedPNTs = get_array(infile, hclBoneSpaceDeformerLocalBlockUnpackedPNT, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} localPNTs=[{localPNTs}], localUnpackedPNTs=[{localUnpackedPNTs}]>".format(**{
            "class_name": self.__class__.__name__,
            "localPNTs": self.localPNTs,
            "localUnpackedPNTs": self.localUnpackedPNTs,
        })
