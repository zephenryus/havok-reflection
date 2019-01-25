from .common import any
import struct


class hkSetunsignedinthkContainerHeapAllocatorhkMapOperationsunsignedint(object):
    elem: any
    numElems: int

    def __init__(self, infile):
        self.elem = any(infile)  # TYPE_ARRAY
        self.numElems = struct.unpack('>i', infile.read(4))
