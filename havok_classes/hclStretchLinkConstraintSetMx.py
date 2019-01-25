from .hclConstraintSet import hclConstraintSet
from typing import List
from .common import get_array
from .hclStretchLinkConstraintSetMxBatch import hclStretchLinkConstraintSetMxBatch
from .hclStretchLinkConstraintSetMxSingle import hclStretchLinkConstraintSetMxSingle


class hclStretchLinkConstraintSetMx(hclConstraintSet):
    batches: List[hclStretchLinkConstraintSetMxBatch]
    singles: List[hclStretchLinkConstraintSetMxSingle]

    def __init__(self, infile):
        self.batches = get_array(infile, hclStretchLinkConstraintSetMxBatch, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.singles = get_array(infile, hclStretchLinkConstraintSetMxSingle, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} batches=[{batches}], singles=[{singles}]>".format(**{
            "class_name": self.__class__.__name__,
            "batches": self.batches,
            "singles": self.singles,
        })
