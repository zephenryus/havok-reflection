from .hkReferencedObject import hkReferencedObject
from .common import any


class hkxVertexSelectionChannel(hkReferencedObject):
    selectedVertices: any

    def __init__(self, infile):
        self.selectedVertices = any(infile)  # TYPE_ARRAY
