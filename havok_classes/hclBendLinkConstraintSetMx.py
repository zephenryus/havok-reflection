from .hclConstraintSet import hclConstraintSet
from typing import List
from .common import get_array
from .hclBendLinkConstraintSetMxBatch import hclBendLinkConstraintSetMxBatch
from .hclBendLinkConstraintSetMxSingle import hclBendLinkConstraintSetMxSingle


class hclBendLinkConstraintSetMx(hclConstraintSet):
    batches: List[hclBendLinkConstraintSetMxBatch]
    singles: List[hclBendLinkConstraintSetMxSingle]

    def __init__(self, infile):
        self.batches = get_array(infile, hclBendLinkConstraintSetMxBatch, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.singles = get_array(infile, hclBendLinkConstraintSetMxSingle, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} batches=[{batches}], singles=[{singles}]>".format(**{
            "class_name": self.__class__.__name__,
            "batches": self.batches,
            "singles": self.singles,
        })
