from .hkReferencedObject import hkReferencedObject
from .common import vector4, any
from .hkaiAgentTraversalInfo import hkaiAgentTraversalInfo
from .hkaiNavVolumePathSearchParameters import hkaiNavVolumePathSearchParameters
from .hkaiSearchParametersSearchBuffers import hkaiSearchParametersSearchBuffers


class hkaiVolumePathfindingUtilFindPathInput(hkReferencedObject):
    startPoint: vector4
    goalPoints: any
    startCellKey: int
    goalCellKeys: any
    maxNumberOfIterations: int
    agentInfo: hkaiAgentTraversalInfo
    searchParameters: hkaiNavVolumePathSearchParameters
    searchBuffers: hkaiSearchParametersSearchBuffers
