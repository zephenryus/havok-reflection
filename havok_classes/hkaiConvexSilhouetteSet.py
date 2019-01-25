from .hkReferencedObject import hkReferencedObject
from .common import any, vector4
from .hkQTransform import hkQTransform
import struct


class hkaiConvexSilhouetteSet(hkReferencedObject):
    vertexPool: any
    silhouetteOffsets: any
    cachedTransform: hkQTransform
    cachedUp: vector4

    def __init__(self, infile):
        self.vertexPool = any(infile)  # TYPE_ARRAY
        self.silhouetteOffsets = any(infile)  # TYPE_ARRAY
        self.cachedTransform = hkQTransform(infile)  # TYPE_STRUCT
        self.cachedUp = struct.unpack('>4f', infile.read(16))
