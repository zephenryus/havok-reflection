from .hclConstraintSet import hclConstraintSet
from .hclCompressibleLinkConstraintSetMxBatch import hclCompressibleLinkConstraintSetMxBatch
from .hclCompressibleLinkConstraintSetMxSingle import hclCompressibleLinkConstraintSetMxSingle


class hclCompressibleLinkConstraintSetMx(hclConstraintSet):
    batches: hclCompressibleLinkConstraintSetMxBatch
    singles: hclCompressibleLinkConstraintSetMxSingle

    def __init__(self, infile):
        self.batches = hclCompressibleLinkConstraintSetMxBatch(infile)  # TYPE_ARRAY
        self.singles = hclCompressibleLinkConstraintSetMxSingle(infile)  # TYPE_ARRAY
