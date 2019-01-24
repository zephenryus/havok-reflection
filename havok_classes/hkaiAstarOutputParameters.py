from enum import Enum
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
