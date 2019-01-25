from .hkReferencedObject import hkReferencedObject
from .common import any


class hkpConvexVerticesConnectivity(hkReferencedObject):
    vertexIndices: any
    numVerticesPerFace: any

    def __init__(self, infile):
        self.vertexIndices = any(infile)  # TYPE_ARRAY
        self.numVerticesPerFace = any(infile)  # TYPE_ARRAY
