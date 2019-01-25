from enum import Enum
import struct
from .enums import SearchStatus, TerminationCause


class SearchStatus(Enum):
    SEARCH_IN_PROGRESS = 0
    SEARCH_SUCCEEDED = 1
    SEARCH_UNREACHABLE = 2
    SEARCH_TERMINATED = 3
    SEARCH_SUCCEEDED_BUT_RESULTS_TRUNCATED = 4
    SEARCH_INVALID = 5


class TerminationCause(Enum):
    NOT_TERMINATED = 0
    TERMINATED_ITERATION_LIMIT = 1
    TERMINATED_OPEN_SET_FULL = 2
    TERMINATED_SEARCH_STATE_FULL = 3
    TERMINATED_BY_USER = 4


class hkaiAstarOutputParameters(object):
    numIterations: int
    goalIndex: int
    pathLength: float
    status: SearchStatus
    terminationCause: TerminationCause

    def __init__(self, infile):
        self.numIterations = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.goalIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.pathLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.status = SearchStatus(infile)  # TYPE_ENUM:TYPE_UINT8
        self.terminationCause = TerminationCause(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} numIterations={numIterations}, goalIndex={goalIndex}, pathLength={pathLength}, status={status}, terminationCause={terminationCause}>".format(**{
            "class_name": self.__class__.__name__,
            "numIterations": self.numIterations,
            "goalIndex": self.goalIndex,
            "pathLength": self.pathLength,
            "status": self.status,
            "terminationCause": self.terminationCause,
        })
