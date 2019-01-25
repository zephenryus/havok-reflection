from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkaiUserEdgeUtilsUserEdgePair import hkaiUserEdgeUtilsUserEdgePair


class hkaiUserEdgePairArray(hkReferencedObject):
    edgePairs: List[hkaiUserEdgeUtilsUserEdgePair]

    def __init__(self, infile):
        self.edgePairs = get_array(infile, hkaiUserEdgeUtilsUserEdgePair, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} edgePairs=[{edgePairs}]>".format(**{
            "class_name": self.__class__.__name__,
            "edgePairs": self.edgePairs,
        })
