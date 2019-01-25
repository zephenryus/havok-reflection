from .hclConstraintSet import hclConstraintSet
from .hclBendLinkConstraintSetLink import hclBendLinkConstraintSetLink


class hclBendLinkConstraintSet(hclConstraintSet):
    links: hclBendLinkConstraintSetLink

    def __init__(self, infile):
        self.links = hclBendLinkConstraintSetLink(infile)  # TYPE_ARRAY
