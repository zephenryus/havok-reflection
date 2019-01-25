from .hclObjectSpaceSkinOperator import hclObjectSpaceSkinOperator
from typing import List
from .common import get_array
from .hclObjectSpaceDeformerLocalBlockPN import hclObjectSpaceDeformerLocalBlockPN
from .hclObjectSpaceDeformerLocalBlockUnpackedPN import hclObjectSpaceDeformerLocalBlockUnpackedPN


class hclObjectSpaceSkinPNOperator(hclObjectSpaceSkinOperator):
    localPNs: List[hclObjectSpaceDeformerLocalBlockPN]
    localUnpackedPNs: List[hclObjectSpaceDeformerLocalBlockUnpackedPN]

    def __init__(self, infile):
        self.localPNs = get_array(infile, hclObjectSpaceDeformerLocalBlockPN, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.localUnpackedPNs = get_array(infile, hclObjectSpaceDeformerLocalBlockUnpackedPN, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} localPNs=[{localPNs}], localUnpackedPNs=[{localUnpackedPNs}]>".format(**{
            "class_name": self.__class__.__name__,
            "localPNs": self.localPNs,
            "localUnpackedPNs": self.localUnpackedPNs,
        })
