from .hclConstraintSet import hclConstraintSet
from typing import List
from .common import get_array
from .hclStretchLinkConstraintSetLink import hclStretchLinkConstraintSetLink


class hclStretchLinkConstraintSet(hclConstraintSet):
    links: List[hclStretchLinkConstraintSetLink]

    def __init__(self, infile):
        self.links = get_array(infile, hclStretchLinkConstraintSetLink, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} links=[{links}]>".format(**{
            "class_name": self.__class__.__name__,
            "links": self.links,
        })
