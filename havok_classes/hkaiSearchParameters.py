from enum import Enum


class ElementSizes(Enum):
    OPENSET_ELEMENT_SIZE = 8
    SEARCH_STATE_ELEMENT_SIZE = 18
    SEARCH_STATE_OVERHEAD = 512


class MemoryDefaultsSingleThreaded(Enum):
    OPEN_SET_SIZE_SINGLE_THREADED = 131072
    SEARCH_STATE_SIZE_SINGLE_THREADED = 590336
    HIERARCHY_OPEN_SET_SIZE_SINGLE_THREADED = 32768
    HIERARCHY_SEARCH_STATE_SIZE_SINGLE_THREADED = 147968


class MemoryDefaultsMultiThreaded(Enum):
    OPEN_SET_SIZE_MULTI_THREADED = 8192
    SEARCH_STATE_SIZE_MULTI_THREADED = 37376
    HIERARCHY_OPEN_SET_SIZE_MULTI_THREADED = 2048
    HIERARCHY_SEARCH_STATE_SIZE_MULTI_THREADED = 9728


class hkaiSearchParameters(object):
    pass

    def __repr__(self):
        return "<{class_name} >".format(**{
            "class_name": self.__class__.__name__,
        })
