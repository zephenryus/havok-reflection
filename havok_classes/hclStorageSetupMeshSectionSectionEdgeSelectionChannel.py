from .hkReferencedObject import hkReferencedObject
from .common import any


class hclStorageSetupMeshSectionSectionEdgeSelectionChannel(hkReferencedObject):
    edgeIndices: any

    def __init__(self, infile):
        self.edgeIndices = any(infile)  # TYPE_ARRAY
