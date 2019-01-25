from .hclConstraintSet import hclConstraintSet
from typing import List
from .common import get_array
from .hclStandardLinkConstraintSetMxBatch import hclStandardLinkConstraintSetMxBatch
from .hclStandardLinkConstraintSetMxSingle import hclStandardLinkConstraintSetMxSingle


class hclStandardLinkConstraintSetMx(hclConstraintSet):
    batches: List[hclStandardLinkConstraintSetMxBatch]
    singles: List[hclStandardLinkConstraintSetMxSingle]

    def __init__(self, infile):
        self.batches = get_array(infile, hclStandardLinkConstraintSetMxBatch, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.singles = get_array(infile, hclStandardLinkConstraintSetMxSingle, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} batches=[{batches}], singles=[{singles}]>".format(**{
            "class_name": self.__class__.__name__,
            "batches": self.batches,
            "singles": self.singles,
        })
