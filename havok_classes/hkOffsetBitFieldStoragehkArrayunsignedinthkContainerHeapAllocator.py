from .common import any
import struct


class hkOffsetBitFieldStoragehkArrayunsignedinthkContainerHeapAllocator(object):
    words: any
    offset: int

    def __init__(self, infile):
        self.words = any(infile)  # TYPE_ARRAY
        self.offset = struct.unpack('>i', infile.read(4))
