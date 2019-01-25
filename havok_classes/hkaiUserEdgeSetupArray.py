from .hkReferencedObject import hkReferencedObject
from .hkaiUserEdgeUtilsUserEdgeSetup import hkaiUserEdgeUtilsUserEdgeSetup


class hkaiUserEdgeSetupArray(hkReferencedObject):
    edgeSetups: hkaiUserEdgeUtilsUserEdgeSetup

    def __init__(self, infile):
        self.edgeSetups = hkaiUserEdgeUtilsUserEdgeSetup(infile)  # TYPE_ARRAY
