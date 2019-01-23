from .hkReferencedObject import hkReferencedObject
from .hkaiEdgePathEdge import hkaiEdgePathEdge


class hkaiEdgePath(hkReferencedObject):
	edges: hkaiEdgePathEdge
	edgeData: any
	edgeDataStriding: int
	leftTurnRadius: float
	rightTurnRadius: float
	characterRadius: float
