from .common import any
import struct


class hkBitFieldStoragehkArrayunsignedinthkContainerHeapAllocator(object):
    words: any
    numBits: int

    def __init__(self, infile):
        self.words = any(infile)  # TYPE_ARRAY
        self.numBits = struct.unpack('>i', infile.read(4))
