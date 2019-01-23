from .hkReferencedObject import hkReferencedObject
from .hkaiNavMeshCutterMeshInfo import hkaiNavMeshCutterMeshInfo
from .hkaiNavMeshCutterSavedConnectivity import hkaiNavMeshCutterSavedConnectivity
from .hkaiStreamingCollection import hkaiStreamingCollection
from .hkaiNavMeshEdgeMatchingParameters import hkaiNavMeshEdgeMatchingParameters


class hkaiNavMeshCutter(hkReferencedObject):
	meshInfos: hkaiNavMeshCutterMeshInfo
	connectivityInfo: hkaiNavMeshCutterSavedConnectivity
	streamingCollection: hkaiStreamingCollection
	forceRecutFaceKeys: any
	forceClearanceCalcFaceKeys: any
	up: any
	edgeMatchParams: hkaiNavMeshEdgeMatchingParameters
	generationSettings: any
	cutEdgeTolerance: float
	minEdgeMatchingLength: float
	smallGapFixupTolerance: float
	performValidationChecks: bool
	clearanceResetMethod: any
	useNewCutter: bool
	domainQuantum: float
