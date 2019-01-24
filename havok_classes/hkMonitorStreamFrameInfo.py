from enum import Enum
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
