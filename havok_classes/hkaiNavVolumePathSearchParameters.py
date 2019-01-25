from enum import Enum
from .common import vector4, any
import struct
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

    def __init__(self, infile):
        self.up = struct.unpack('>4f', infile.read(16))
        self.costModifier = any(infile)  # TYPE_POINTER
        self.edgeFilter = any(infile)  # TYPE_POINTER
        self.lineOfSightFlags = any(infile)  # TYPE_FLAGS
        self.heuristicWeight = struct.unpack('>f', infile.read(4))
        self.maximumPathLength = struct.unpack('>f', infile.read(4))
        self.bufferSizes = hkaiSearchParametersBufferSizes(infile)  # TYPE_STRUCT
