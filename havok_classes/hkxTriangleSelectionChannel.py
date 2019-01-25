from .hkReferencedObject import hkReferencedObject
from .common import any


class hkxTriangleSelectionChannel(hkReferencedObject):
    selectedTriangles: any

    def __init__(self, infile):
        self.selectedTriangles = any(infile)  # TYPE_ARRAY
