from enum import Enum


class ThreadingType(Enum):
    SINGLE_THREADED = 0
    MULTI_THREADED = 1


class SearchType(Enum):
    SEARCH_REGULAR = 0
    SEARCH_HIERARCHICAL = 1


class hkaiSearchParametersBufferSizes(object):
    maxOpenSetSizeBytes: int
    maxSearchStateSizeBytes: int
