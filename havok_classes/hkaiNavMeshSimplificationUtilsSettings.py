from .hkaiNavMeshSimplificationUtilsExtraVertexSettings import hkaiNavMeshSimplificationUtilsExtraVertexSettings


class hkaiNavMeshSimplificationUtilsSettings(object):
	maxBorderSimplifyArea: float
	maxConcaveBorderSimplifyArea: float
	minCorridorWidth: float
	maxCorridorWidth: float
	holeReplacementArea: float
	aabbReplacementAreaFraction: float
	maxLoopShrinkFraction: float
	maxBorderHeightError: float
	maxBorderDistanceError: float
	maxPartitionSize: int
	useHeightPartitioning: bool
	maxPartitionHeightError: float
	useConservativeHeightPartitioning: bool
	hertelMehlhornHeightError: float
	cosPlanarityThreshold: float
	nonconvexityThreshold: float
	boundaryEdgeFilterThreshold: float
	maxSharedVertexHorizontalError: float
	maxSharedVertexVerticalError: float
	maxBoundaryVertexHorizontalError: float
	maxBoundaryVertexVerticalError: float
	mergeLongestEdgesFirst: bool
	extraVertexSettings: hkaiNavMeshSimplificationUtilsExtraVertexSettings
	saveInputSnapshot: bool
	snapshotFilename: any
