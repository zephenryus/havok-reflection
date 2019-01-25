from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array


class hkpConvexVerticesConnectivity(hkReferencedObject):
    vertexIndices: List[int]
    numVerticesPerFace: List[int]

    def __init__(self, infile):
        self.vertexIndices = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.numVerticesPerFace = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} vertexIndices=[{vertexIndices}], numVerticesPerFace=[{numVerticesPerFace}]>".format(**{
            "class_name": self.__class__.__name__,
            "vertexIndices": self.vertexIndices,
            "numVerticesPerFace": self.numVerticesPerFace,
        })
