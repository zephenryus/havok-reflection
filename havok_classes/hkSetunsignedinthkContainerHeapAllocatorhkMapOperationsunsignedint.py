from typing import List
from .common import get_array
import struct


class hkSetunsignedinthkContainerHeapAllocatorhkMapOperationsunsignedint(object):
    elem: List[int]
    numElems: int

    def __init__(self, infile):
        self.elem = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.numElems = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} elem=[{elem}], numElems={numElems}>".format(**{
            "class_name": self.__class__.__name__,
            "elem": self.elem,
            "numElems": self.numElems,
        })
