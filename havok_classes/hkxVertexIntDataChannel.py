from .hkReferencedObject import hkReferencedObject
from .common import any


class hkxVertexIntDataChannel(hkReferencedObject):
    perVertexInts: any

    def __init__(self, infile):
        self.perVertexInts = any(infile)  # TYPE_ARRAY
