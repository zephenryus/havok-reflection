from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkaiUserEdgeUtilsUserEdgeSetup import hkaiUserEdgeUtilsUserEdgeSetup


class hkaiUserEdgeSetupArray(hkReferencedObject):
    edgeSetups: List[hkaiUserEdgeUtilsUserEdgeSetup]

    def __init__(self, infile):
        self.edgeSetups = get_array(infile, hkaiUserEdgeUtilsUserEdgeSetup, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} edgeSetups=[{edgeSetups}]>".format(**{
            "class_name": self.__class__.__name__,
            "edgeSetups": self.edgeSetups,
        })
