from .common import any
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
