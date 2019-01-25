from enum import Enum
import struct


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

    def __init__(self, infile):
        self.threadId = struct.unpack('>I', infile.read(4))
        self.stackTraceId = struct.unpack('>i', infile.read(4))
        self.markCount = struct.unpack('>H', infile.read(2))
        self.markBitStack = struct.unpack('>H', infile.read(2))
