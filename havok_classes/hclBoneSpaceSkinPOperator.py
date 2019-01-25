from .hclBoneSpaceSkinOperator import hclBoneSpaceSkinOperator
from typing import List
from .common import get_array
from .hclBoneSpaceDeformerLocalBlockP import hclBoneSpaceDeformerLocalBlockP
from .hclBoneSpaceDeformerLocalBlockUnpackedP import hclBoneSpaceDeformerLocalBlockUnpackedP


class hclBoneSpaceSkinPOperator(hclBoneSpaceSkinOperator):
    localPs: List[hclBoneSpaceDeformerLocalBlockP]
    localUnpackedPs: List[hclBoneSpaceDeformerLocalBlockUnpackedP]

    def __init__(self, infile):
        self.localPs = get_array(infile, hclBoneSpaceDeformerLocalBlockP, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.localUnpackedPs = get_array(infile, hclBoneSpaceDeformerLocalBlockUnpackedP, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} localPs=[{localPs}], localUnpackedPs=[{localUnpackedPs}]>".format(**{
            "class_name": self.__class__.__name__,
            "localPs": self.localPs,
            "localUnpackedPs": self.localUnpackedPs,
        })
