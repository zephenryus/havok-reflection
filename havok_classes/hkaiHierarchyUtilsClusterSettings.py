import struct
from .hkaiNavMeshPathSearchParameters import hkaiNavMeshPathSearchParameters
from .hkaiAgentTraversalInfo import hkaiAgentTraversalInfo


class hkaiHierarchyUtilsClusterSettings(object):
    desiredFacesPerCluster: int
    searchParameters: hkaiNavMeshPathSearchParameters
    agentInfo: hkaiAgentTraversalInfo

    def __init__(self, infile):
        self.desiredFacesPerCluster = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.searchParameters = hkaiNavMeshPathSearchParameters(infile)  # TYPE_STRUCT:TYPE_VOID
        self.agentInfo = hkaiAgentTraversalInfo(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} desiredFacesPerCluster={desiredFacesPerCluster}, searchParameters={searchParameters}, agentInfo={agentInfo}>".format(**{
            "class_name": self.__class__.__name__,
            "desiredFacesPerCluster": self.desiredFacesPerCluster,
            "searchParameters": self.searchParameters,
            "agentInfo": self.agentInfo,
        })
