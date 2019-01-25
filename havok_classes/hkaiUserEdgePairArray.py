from .hkReferencedObject import hkReferencedObject
from .hkaiUserEdgeUtilsUserEdgePair import hkaiUserEdgeUtilsUserEdgePair


class hkaiUserEdgePairArray(hkReferencedObject):
    edgePairs: hkaiUserEdgeUtilsUserEdgePair

    def __init__(self, infile):
        self.edgePairs = hkaiUserEdgeUtilsUserEdgePair(infile)  # TYPE_ARRAY
