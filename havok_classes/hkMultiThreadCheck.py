from enum import Enum


class AccessType(Enum):
    HK_ACCESS_IGNORE = 0
    HK_ACCESS_RO = 1
    HK_ACCESS_RW = 2


class ReadMode(Enum):
    THIS_OBJECT_ONLY = 0
    RECURSIVE = 1


class hkMultiThreadCheck(object):
    threadId: int
    stackTraceId: int
    markCount: int
    markBitStack: int
