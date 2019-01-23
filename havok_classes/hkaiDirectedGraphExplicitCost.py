from .hkReferencedObject import hkReferencedObject
from .hkaiDirectedGraphExplicitCostNode import hkaiDirectedGraphExplicitCostNode
from .hkaiDirectedGraphExplicitCostEdge import hkaiDirectedGraphExplicitCostEdge
from .hkaiStreamingSet import hkaiStreamingSet


class hkaiDirectedGraphExplicitCost(hkReferencedObject):
	positions: any
	nodes: hkaiDirectedGraphExplicitCostNode
	edges: hkaiDirectedGraphExplicitCostEdge
	nodeData: any
	edgeData: any
	nodeDataStriding: int
	edgeDataStriding: int
	streamingSets: hkaiStreamingSet
