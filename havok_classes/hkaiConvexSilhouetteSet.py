from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkQTransform import hkQTransform
import struct


class hkaiConvexSilhouetteSet(hkReferencedObject):
    vertexPool: List[vector4]
    silhouetteOffsets: List[int]
    cachedTransform: hkQTransform
    cachedUp: vector4

    def __init__(self, infile):
        self.vertexPool = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.silhouetteOffsets = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32
        self.cachedTransform = hkQTransform(infile)  # TYPE_STRUCT:TYPE_VOID
        self.cachedUp = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} vertexPool=[{vertexPool}], silhouetteOffsets=[{silhouetteOffsets}], cachedTransform={cachedTransform}, cachedUp={cachedUp}>".format(**{
            "class_name": self.__class__.__name__,
            "vertexPool": self.vertexPool,
            "silhouetteOffsets": self.silhouetteOffsets,
            "cachedTransform": self.cachedTransform,
            "cachedUp": self.cachedUp,
        })
