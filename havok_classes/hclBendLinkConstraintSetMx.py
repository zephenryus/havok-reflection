from .hclConstraintSet import hclConstraintSet
from .hclBendLinkConstraintSetMxBatch import hclBendLinkConstraintSetMxBatch
from .hclBendLinkConstraintSetMxSingle import hclBendLinkConstraintSetMxSingle


class hclBendLinkConstraintSetMx(hclConstraintSet):
    batches: hclBendLinkConstraintSetMxBatch
    singles: hclBendLinkConstraintSetMxSingle

    def __init__(self, infile):
        self.batches = hclBendLinkConstraintSetMxBatch(infile)  # TYPE_ARRAY
        self.singles = hclBendLinkConstraintSetMxSingle(infile)  # TYPE_ARRAY
