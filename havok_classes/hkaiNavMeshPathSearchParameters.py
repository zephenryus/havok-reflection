from .hkaiSearchParametersBufferSizes import hkaiSearchParametersBufferSizes
from .hkaiSearchParametersBufferSizes import hkaiSearchParametersBufferSizes


class hkaiNavMeshPathSearchParameters(object):
	up: any
	costModifier: any
	edgeFilter: any
	validateInputs: bool
	outputPathFlags: any
	lineOfSightFlags: any
	useHierarchicalHeuristic: bool
	projectedRadiusCheck: bool
	useGrandparentDistanceCalculation: bool
	heuristicWeight: float
	simpleRadiusThreshold: float
	maximumPathLength: float
	searchSphereRadius: float
	searchCapsuleRadius: float
	bufferSizes: hkaiSearchParametersBufferSizes
	hierarchyBufferSizes: hkaiSearchParametersBufferSizes
