from typing import List
from .common import get_array
import struct


class hkBitFieldStoragehkArrayunsignedinthkContainerHeapAllocator(object):
    words: List[int]
    numBits: int

    def __init__(self, infile):
        self.words = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.numBits = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} words=[{words}], numBits={numBits}>".format(**{
            "class_name": self.__class__.__name__,
            "words": self.words,
            "numBits": self.numBits,
        })
