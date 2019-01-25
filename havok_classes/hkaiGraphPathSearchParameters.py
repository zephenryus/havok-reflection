import struct
from .common import any
from .hkaiSearchParametersBufferSizes import hkaiSearchParametersBufferSizes


class hkaiGraphPathSearchParameters(object):
    heuristicWeight: float
    useHierarchicalHeuristic: bool
    costModifier: any
    edgeFilter: any
    bufferSizes: hkaiSearchParametersBufferSizes
    hierarchyBufferSizes: hkaiSearchParametersBufferSizes

    def __init__(self, infile):
        self.heuristicWeight = struct.unpack('>f', infile.read(4))
        self.useHierarchicalHeuristic = struct.unpack('>?', infile.read(1))
        self.costModifier = any(infile)  # TYPE_POINTER
        self.edgeFilter = any(infile)  # TYPE_POINTER
        self.bufferSizes = hkaiSearchParametersBufferSizes(infile)  # TYPE_STRUCT
        self.hierarchyBufferSizes = hkaiSearchParametersBufferSizes(infile)  # TYPE_STRUCT
