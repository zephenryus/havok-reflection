from .hkReferencedObject import hkReferencedObject
from .common import vector4, any
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
