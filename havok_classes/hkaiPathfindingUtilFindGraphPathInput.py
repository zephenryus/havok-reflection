from typing import List
from .common import get_array
import struct
from .hkaiAgentTraversalInfo import hkaiAgentTraversalInfo
from .hkaiGraphPathSearchParameters import hkaiGraphPathSearchParameters
from .hkaiSearchParametersSearchBuffers import hkaiSearchParametersSearchBuffers


class hkaiPathfindingUtilFindGraphPathInput(object):
    startNodeKeys: List[int]
    initialCosts: List[float]
    goalNodeKeys: List[int]
    finalCosts: List[float]
    maxNumberOfIterations: int
    agentInfo: hkaiAgentTraversalInfo
    searchParameters: hkaiGraphPathSearchParameters
    searchBuffers: hkaiSearchParametersSearchBuffers
    hierarchySearchBuffers: hkaiSearchParametersSearchBuffers

    def __init__(self, infile):
        self.startNodeKeys = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.initialCosts = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.goalNodeKeys = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.finalCosts = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.maxNumberOfIterations = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.agentInfo = hkaiAgentTraversalInfo(infile)  # TYPE_STRUCT:TYPE_VOID
        self.searchParameters = hkaiGraphPathSearchParameters(infile)  # TYPE_STRUCT:TYPE_VOID
        self.searchBuffers = hkaiSearchParametersSearchBuffers(infile)  # TYPE_STRUCT:TYPE_VOID
        self.hierarchySearchBuffers = hkaiSearchParametersSearchBuffers(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} startNodeKeys=[{startNodeKeys}], initialCosts=[{initialCosts}], goalNodeKeys=[{goalNodeKeys}], finalCosts=[{finalCosts}], maxNumberOfIterations={maxNumberOfIterations}, agentInfo={agentInfo}, searchParameters={searchParameters}, searchBuffers={searchBuffers}, hierarchySearchBuffers={hierarchySearchBuffers}>".format(**{
            "class_name": self.__class__.__name__,
            "startNodeKeys": self.startNodeKeys,
            "initialCosts": self.initialCosts,
            "goalNodeKeys": self.goalNodeKeys,
            "finalCosts": self.finalCosts,
            "maxNumberOfIterations": self.maxNumberOfIterations,
            "agentInfo": self.agentInfo,
            "searchParameters": self.searchParameters,
            "searchBuffers": self.searchBuffers,
            "hierarchySearchBuffers": self.hierarchySearchBuffers,
        })
