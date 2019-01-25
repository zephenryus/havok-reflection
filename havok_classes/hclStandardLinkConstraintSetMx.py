from .hclConstraintSet import hclConstraintSet
from .hclStandardLinkConstraintSetMxBatch import hclStandardLinkConstraintSetMxBatch
from .hclStandardLinkConstraintSetMxSingle import hclStandardLinkConstraintSetMxSingle


class hclStandardLinkConstraintSetMx(hclConstraintSet):
    batches: hclStandardLinkConstraintSetMxBatch
    singles: hclStandardLinkConstraintSetMxSingle

    def __init__(self, infile):
        self.batches = hclStandardLinkConstraintSetMxBatch(infile)  # TYPE_ARRAY
        self.singles = hclStandardLinkConstraintSetMxSingle(infile)  # TYPE_ARRAY
