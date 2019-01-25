import struct
from .hkaiNavMeshPathSearchParameters import hkaiNavMeshPathSearchParameters
from .hkaiAgentTraversalInfo import hkaiAgentTraversalInfo


class hkaiHierarchyUtilsClusterSettings(object):
    desiredFacesPerCluster: int
    searchParameters: hkaiNavMeshPathSearchParameters
    agentInfo: hkaiAgentTraversalInfo

    def __init__(self, infile):
        self.desiredFacesPerCluster = struct.unpack('>i', infile.read(4))
        self.searchParameters = hkaiNavMeshPathSearchParameters(infile)  # TYPE_STRUCT
        self.agentInfo = hkaiAgentTraversalInfo(infile)  # TYPE_STRUCT
