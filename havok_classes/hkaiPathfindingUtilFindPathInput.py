from .hkReferencedObject import hkReferencedObject
from .common import vector4, any
import struct
from .hkaiAgentTraversalInfo import hkaiAgentTraversalInfo
from .hkaiNavMeshPathSearchParameters import hkaiNavMeshPathSearchParameters
from .hkaiSearchParametersSearchBuffers import hkaiSearchParametersSearchBuffers


class hkaiPathfindingUtilFindPathInput(hkReferencedObject):
    startPoint: vector4
    goalPoints: any
    startFaceKey: int
    goalFaceKeys: any
    maxNumberOfIterations: int
    agentInfo: hkaiAgentTraversalInfo
    searchParameters: hkaiNavMeshPathSearchParameters
    searchBuffers: hkaiSearchParametersSearchBuffers
    hierarchySearchBuffers: hkaiSearchParametersSearchBuffers

    def __init__(self, infile):
        self.startPoint = struct.unpack('>4f', infile.read(16))
        self.goalPoints = any(infile)  # TYPE_ARRAY
        self.startFaceKey = struct.unpack('>I', infile.read(4))
        self.goalFaceKeys = any(infile)  # TYPE_ARRAY
        self.maxNumberOfIterations = struct.unpack('>i', infile.read(4))
        self.agentInfo = hkaiAgentTraversalInfo(infile)  # TYPE_STRUCT
        self.searchParameters = hkaiNavMeshPathSearchParameters(infile)  # TYPE_STRUCT
        self.searchBuffers = hkaiSearchParametersSearchBuffers(infile)  # TYPE_STRUCT
        self.hierarchySearchBuffers = hkaiSearchParametersSearchBuffers(infile)  # TYPE_STRUCT
