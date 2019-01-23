from .hkaiAgentTraversalInfo import hkaiAgentTraversalInfo
from .hkaiAstarCostModifier import hkaiAstarCostModifier
from .hkaiAstarEdgeFilter import hkaiAstarEdgeFilter


class hkaiLineOfSightUtilInputBase(object):
	startPoint: any
	up: any
	startFaceKey: int
	maxNumberOfIterations: int
	agentInfo: hkaiAgentTraversalInfo
	searchRadius: float
	maximumPathLength: float
	costModifier: hkaiAstarCostModifier
	edgeFilter: hkaiAstarEdgeFilter
	outputEdgesOnFailure: bool
	projectedRadiusCheck: bool
	exactInternalVertexHandling: bool
	isWallClimbing: bool
	mode: any
	userEdgeHandling: any
	ignoreBackfacingEdges: bool
