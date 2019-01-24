from .hclConstraintSet import hclConstraintSet
from .hclBendLinkConstraintSetMxBatch import hclBendLinkConstraintSetMxBatch
from .hclBendLinkConstraintSetMxSingle import hclBendLinkConstraintSetMxSingle


class hclBendLinkConstraintSetMx(hclConstraintSet):
    batches: hclBendLinkConstraintSetMxBatch
    singles: hclBendLinkConstraintSetMxSingle
