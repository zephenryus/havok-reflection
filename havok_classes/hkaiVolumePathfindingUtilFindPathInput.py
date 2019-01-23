from .hkReferencedObject import hkReferencedObject
from .hkaiAgentTraversalInfo import hkaiAgentTraversalInfo
from .hkaiNavVolumePathSearchParameters import hkaiNavVolumePathSearchParameters
from .hkaiSearchParametersSearchBuffers import hkaiSearchParametersSearchBuffers


class hkaiVolumePathfindingUtilFindPathInput(hkReferencedObject):
	startPoint: any
	goalPoints: any
	startCellKey: int
	goalCellKeys: any
	maxNumberOfIterations: int
	agentInfo: hkaiAgentTraversalInfo
	searchParameters: hkaiNavVolumePathSearchParameters
	searchBuffers: hkaiSearchParametersSearchBuffers
