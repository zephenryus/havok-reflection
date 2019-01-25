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
        self.maxOpenSetSizeBytes = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.maxSearchStateSizeBytes = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} maxOpenSetSizeBytes={maxOpenSetSizeBytes}, maxSearchStateSizeBytes={maxSearchStateSizeBytes}>".format(**{
            "class_name": self.__class__.__name__,
            "maxOpenSetSizeBytes": self.maxOpenSetSizeBytes,
            "maxSearchStateSizeBytes": self.maxSearchStateSizeBytes,
        })
