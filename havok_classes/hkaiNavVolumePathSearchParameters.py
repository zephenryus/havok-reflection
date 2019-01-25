from enum import Enum
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
        self.up = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.costModifier = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.edgeFilter = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.lineOfSightFlags = any(infile)  # TYPE_FLAGS:TYPE_UINT8
        self.heuristicWeight = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maximumPathLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.bufferSizes = hkaiSearchParametersBufferSizes(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} up={up}, costModifier={costModifier}, edgeFilter={edgeFilter}, lineOfSightFlags={lineOfSightFlags}, heuristicWeight={heuristicWeight}, maximumPathLength={maximumPathLength}, bufferSizes={bufferSizes}>".format(**{
            "class_name": self.__class__.__name__,
            "up": self.up,
            "costModifier": self.costModifier,
            "edgeFilter": self.edgeFilter,
            "lineOfSightFlags": self.lineOfSightFlags,
            "heuristicWeight": self.heuristicWeight,
            "maximumPathLength": self.maximumPathLength,
            "bufferSizes": self.bufferSizes,
        })
