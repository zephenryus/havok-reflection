from .hkReferencedObject import hkReferencedObject
from .hkaiNavMeshClearanceCacheMcpDataInteger import hkaiNavMeshClearanceCacheMcpDataInteger


class hkaiNavMeshClearanceCache(hkReferencedObject):
	clearanceCeiling: float
	clearanceIntToRealMultiplier: float
	clearanceRealToIntMultiplier: float
	faceOffsets: any
	edgePairClearances: any
	unusedEdgePairElements: int
	mcpData: hkaiNavMeshClearanceCacheMcpDataInteger
	vertexClearances: any
