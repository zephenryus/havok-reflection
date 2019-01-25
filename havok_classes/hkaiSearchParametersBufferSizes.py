from enum import Enum
import struct


class ThreadingType(Enum):
    SINGLE_THREADED = 0
    MULTI_THREADED = 1


class SearchType(Enum):
    SEARCH_REGULAR = 0
    SEARCH_HIERARCHICAL = 1


class hkaiSearchParametersBufferSizes(object):
    maxOpenSetSizeBytes: int
    maxSearchStateSizeBytes: int

    def __init__(self, infile):
        self.maxOpenSetSizeBytes = struct.unpack('>i', infile.read(4))
        self.maxSearchStateSizeBytes = struct.unpack('>i', infile.read(4))
