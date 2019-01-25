from enum import Enum
import struct
from .enums import AbsoluteTimeCounter


class AbsoluteTimeCounter(Enum):
    ABSOLUTE_TIME_TIMER_0 = 0
    ABSOLUTE_TIME_TIMER_1 = 1
    ABSOLUTE_TIME_NOT_TIMED = 4294967295


class hkMonitorStreamFrameInfo(object):
    heading: str
    indexOfTimer0: int
    indexOfTimer1: int
    absoluteTimeCounter: AbsoluteTimeCounter
    timerFactor0: float
    timerFactor1: float
    threadId: int
    frameStreamStart: int
    frameStreamEnd: int

    def __init__(self, infile):
        self.heading = struct.unpack('>s', infile.read(0))
        self.indexOfTimer0 = struct.unpack('>i', infile.read(4))
        self.indexOfTimer1 = struct.unpack('>i', infile.read(4))
        self.absoluteTimeCounter = AbsoluteTimeCounter(infile)  # TYPE_ENUM
        self.timerFactor0 = struct.unpack('>f', infile.read(4))
        self.timerFactor1 = struct.unpack('>f', infile.read(4))
        self.threadId = struct.unpack('>i', infile.read(4))
        self.frameStreamStart = struct.unpack('>i', infile.read(4))
        self.frameStreamEnd = struct.unpack('>i', infile.read(4))
