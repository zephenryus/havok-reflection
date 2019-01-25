from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array


class hkxVertexVectorDataChannel(hkReferencedObject):
    perVertexVectors: List[float]

    def __init__(self, infile):
        self.perVertexVectors = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL

    def __repr__(self):
        return "<{class_name} perVertexVectors=[{perVertexVectors}]>".format(**{
            "class_name": self.__class__.__name__,
            "perVertexVectors": self.perVertexVectors,
        })
