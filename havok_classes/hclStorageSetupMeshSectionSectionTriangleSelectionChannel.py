from .hkReferencedObject import hkReferencedObject
from .common import any


class hclStorageSetupMeshSectionSectionTriangleSelectionChannel(hkReferencedObject):
    triangleIndices: any

    def __init__(self, infile):
        self.triangleIndices = any(infile)  # TYPE_ARRAY
