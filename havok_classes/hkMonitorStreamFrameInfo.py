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
        self.heading = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.indexOfTimer0 = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.indexOfTimer1 = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.absoluteTimeCounter = AbsoluteTimeCounter(infile)  # TYPE_ENUM:TYPE_UINT32
        self.timerFactor0 = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.timerFactor1 = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.threadId = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.frameStreamStart = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.frameStreamEnd = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} heading=\"{heading}\", indexOfTimer0={indexOfTimer0}, indexOfTimer1={indexOfTimer1}, absoluteTimeCounter={absoluteTimeCounter}, timerFactor0={timerFactor0}, timerFactor1={timerFactor1}, threadId={threadId}, frameStreamStart={frameStreamStart}, frameStreamEnd={frameStreamEnd}>".format(**{
            "class_name": self.__class__.__name__,
            "heading": self.heading,
            "indexOfTimer0": self.indexOfTimer0,
            "indexOfTimer1": self.indexOfTimer1,
            "absoluteTimeCounter": self.absoluteTimeCounter,
            "timerFactor0": self.timerFactor0,
            "timerFactor1": self.timerFactor1,
            "threadId": self.threadId,
            "frameStreamStart": self.frameStreamStart,
            "frameStreamEnd": self.frameStreamEnd,
        })
