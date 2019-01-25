from .hkReferencedObject import hkReferencedObject
from .common import any


class hkxVertexVectorDataChannel(hkReferencedObject):
    perVertexVectors: any

    def __init__(self, infile):
        self.perVertexVectors = any(infile)  # TYPE_ARRAY
