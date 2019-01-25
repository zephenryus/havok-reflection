from .common import any
import struct
from .hkaiAgentTraversalInfo import hkaiAgentTraversalInfo
from .hkaiGraphPathSearchParameters import hkaiGraphPathSearchParameters
from .hkaiSearchParametersSearchBuffers import hkaiSearchParametersSearchBuffers


class hkaiPathfindingUtilFindGraphPathInput(object):
    startNodeKeys: any
    initialCosts: any
    goalNodeKeys: any
    finalCosts: any
    maxNumberOfIterations: int
    agentInfo: hkaiAgentTraversalInfo
    searchParameters: hkaiGraphPathSearchParameters
    searchBuffers: hkaiSearchParametersSearchBuffers
    hierarchySearchBuffers: hkaiSearchParametersSearchBuffers

    def __init__(self, infile):
        self.startNodeKeys = any(infile)  # TYPE_ARRAY
        self.initialCosts = any(infile)  # TYPE_ARRAY
        self.goalNodeKeys = any(infile)  # TYPE_ARRAY
        self.finalCosts = any(infile)  # TYPE_ARRAY
        self.maxNumberOfIterations = struct.unpack('>i', infile.read(4))
        self.agentInfo = hkaiAgentTraversalInfo(infile)  # TYPE_STRUCT
        self.searchParameters = hkaiGraphPathSearchParameters(infile)  # TYPE_STRUCT
        self.searchBuffers = hkaiSearchParametersSearchBuffers(infile)  # TYPE_STRUCT
        self.hierarchySearchBuffers = hkaiSearchParametersSearchBuffers(infile)  # TYPE_STRUCT
