from .hclConstraintSet import hclConstraintSet
from .hclCompressibleLinkConstraintSetLink import hclCompressibleLinkConstraintSetLink


class hclCompressibleLinkConstraintSet(hclConstraintSet):
    links: hclCompressibleLinkConstraintSetLink

    def __init__(self, infile):
        self.links = hclCompressibleLinkConstraintSetLink(infile)  # TYPE_ARRAY
