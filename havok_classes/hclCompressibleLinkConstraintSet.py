from .hclConstraintSet import hclConstraintSet
from typing import List
from .common import get_array
from .hclCompressibleLinkConstraintSetLink import hclCompressibleLinkConstraintSetLink


class hclCompressibleLinkConstraintSet(hclConstraintSet):
    links: List[hclCompressibleLinkConstraintSetLink]

    def __init__(self, infile):
        self.links = get_array(infile, hclCompressibleLinkConstraintSetLink, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} links=[{links}]>".format(**{
            "class_name": self.__class__.__name__,
            "links": self.links,
        })
