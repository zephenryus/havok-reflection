from .hclConstraintSet import hclConstraintSet
from typing import List
from .common import get_array
from .hclCompressibleLinkConstraintSetMxBatch import hclCompressibleLinkConstraintSetMxBatch
from .hclCompressibleLinkConstraintSetMxSingle import hclCompressibleLinkConstraintSetMxSingle


class hclCompressibleLinkConstraintSetMx(hclConstraintSet):
    batches: List[hclCompressibleLinkConstraintSetMxBatch]
    singles: List[hclCompressibleLinkConstraintSetMxSingle]

    def __init__(self, infile):
        self.batches = get_array(infile, hclCompressibleLinkConstraintSetMxBatch, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.singles = get_array(infile, hclCompressibleLinkConstraintSetMxSingle, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} batches=[{batches}], singles=[{singles}]>".format(**{
            "class_name": self.__class__.__name__,
            "batches": self.batches,
            "singles": self.singles,
        })
