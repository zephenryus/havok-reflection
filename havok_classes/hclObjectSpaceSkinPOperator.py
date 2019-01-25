from .hclObjectSpaceSkinOperator import hclObjectSpaceSkinOperator
from typing import List
from .common import get_array
from .hclObjectSpaceDeformerLocalBlockP import hclObjectSpaceDeformerLocalBlockP
from .hclObjectSpaceDeformerLocalBlockUnpackedP import hclObjectSpaceDeformerLocalBlockUnpackedP


class hclObjectSpaceSkinPOperator(hclObjectSpaceSkinOperator):
    localPs: List[hclObjectSpaceDeformerLocalBlockP]
    localUnpackedPs: List[hclObjectSpaceDeformerLocalBlockUnpackedP]

    def __init__(self, infile):
        self.localPs = get_array(infile, hclObjectSpaceDeformerLocalBlockP, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.localUnpackedPs = get_array(infile, hclObjectSpaceDeformerLocalBlockUnpackedP, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} localPs=[{localPs}], localUnpackedPs=[{localUnpackedPs}]>".format(**{
            "class_name": self.__class__.__name__,
            "localPs": self.localPs,
            "localUnpackedPs": self.localUnpackedPs,
        })
