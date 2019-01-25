from .hclConstraintSet import hclConstraintSet
from .hclStretchLinkConstraintSetMxBatch import hclStretchLinkConstraintSetMxBatch
from .hclStretchLinkConstraintSetMxSingle import hclStretchLinkConstraintSetMxSingle


class hclStretchLinkConstraintSetMx(hclConstraintSet):
    batches: hclStretchLinkConstraintSetMxBatch
    singles: hclStretchLinkConstraintSetMxSingle

    def __init__(self, infile):
        self.batches = hclStretchLinkConstraintSetMxBatch(infile)  # TYPE_ARRAY
        self.singles = hclStretchLinkConstraintSetMxSingle(infile)  # TYPE_ARRAY
