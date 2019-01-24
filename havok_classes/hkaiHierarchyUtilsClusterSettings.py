from .hkaiNavMeshPathSearchParameters import hkaiNavMeshPathSearchParameters
from .hkaiAgentTraversalInfo import hkaiAgentTraversalInfo


class hkaiHierarchyUtilsClusterSettings(object):
    desiredFacesPerCluster: int
    searchParameters: hkaiNavMeshPathSearchParameters
    agentInfo: hkaiAgentTraversalInfo
