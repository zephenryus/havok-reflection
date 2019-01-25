from .hkIntRealPair import hkIntRealPair
import struct


class hkSethkIntRealPairhkContainerHeapAllocatorhkMapOperationshkIntRealPair(object):
    elem: hkIntRealPair
    numElems: int

    def __init__(self, infile):
        self.elem = hkIntRealPair(infile)  # TYPE_ARRAY
        self.numElems = struct.unpack('>i', infile.read(4))
