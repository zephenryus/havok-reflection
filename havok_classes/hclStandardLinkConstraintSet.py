from .hclConstraintSet import hclConstraintSet
from .hclStandardLinkConstraintSetLink import hclStandardLinkConstraintSetLink


class hclStandardLinkConstraintSet(hclConstraintSet):
    links: hclStandardLinkConstraintSetLink

    def __init__(self, infile):
        self.links = hclStandardLinkConstraintSetLink(infile)  # TYPE_ARRAY
