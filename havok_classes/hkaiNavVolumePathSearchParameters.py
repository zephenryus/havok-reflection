from enum import Enum
from .common import vector4, any
from .hkaiSearchParametersBufferSizes import hkaiSearchParametersBufferSizes


class LineOfSightFlags(Enum):
    NO_LINE_OF_SIGHT_CHECK = 0
    EARLY_OUT_IF_NO_COST_MODIFIER = 1
    EARLY_OUT_ALWAYS = 4


class hkaiNavVolumePathSearchParameters(object):
    up: vector4
    costModifier: any
    edgeFilter: any
    lineOfSightFlags: any
    heuristicWeight: float
    maximumPathLength: float
    bufferSizes: hkaiSearchParametersBufferSizes
