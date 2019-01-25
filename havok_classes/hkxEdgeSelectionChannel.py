from .hkReferencedObject import hkReferencedObject
from .common import any


class hkxEdgeSelectionChannel(hkReferencedObject):
    selectedEdges: any

    def __init__(self, infile):
        self.selectedEdges = any(infile)  # TYPE_ARRAY
