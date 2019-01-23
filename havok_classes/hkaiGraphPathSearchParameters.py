from .hkaiSearchParametersBufferSizes import hkaiSearchParametersBufferSizes
from .hkaiSearchParametersBufferSizes import hkaiSearchParametersBufferSizes


class hkaiGraphPathSearchParameters(object):
	heuristicWeight: float
	useHierarchicalHeuristic: bool
	costModifier: any
	edgeFilter: any
	bufferSizes: hkaiSearchParametersBufferSizes
	hierarchyBufferSizes: hkaiSearchParametersBufferSizes
