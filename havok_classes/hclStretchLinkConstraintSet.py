from .hclConstraintSet import hclConstraintSet
from .hclStretchLinkConstraintSetLink import hclStretchLinkConstraintSetLink


class hclStretchLinkConstraintSet(hclConstraintSet):
    links: hclStretchLinkConstraintSetLink

    def __init__(self, infile):
        self.links = hclStretchLinkConstraintSetLink(infile)  # TYPE_ARRAY
