from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array


class hkxVertexIntDataChannel(hkReferencedObject):
    perVertexInts: List[int]

    def __init__(self, infile):
        self.perVertexInts = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32

    def __repr__(self):
        return "<{class_name} perVertexInts=[{perVertexInts}]>".format(**{
            "class_name": self.__class__.__name__,
            "perVertexInts": self.perVertexInts,
        })
