from typing import List
from .common import get_array
from .hkIntRealPair import hkIntRealPair
import struct


class hkSethkIntRealPairhkContainerHeapAllocatorhkMapOperationshkIntRealPair(object):
    elem: List[hkIntRealPair]
    numElems: int

    def __init__(self, infile):
        self.elem = get_array(infile, hkIntRealPair, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.numElems = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} elem=[{elem}], numElems={numElems}>".format(**{
            "class_name": self.__class__.__name__,
            "elem": self.elem,
            "numElems": self.numElems,
        })
