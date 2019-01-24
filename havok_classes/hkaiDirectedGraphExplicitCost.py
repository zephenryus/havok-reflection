from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .common import any
from .hkaiDirectedGraphExplicitCostNode import hkaiDirectedGraphExplicitCostNode
from .hkaiDirectedGraphExplicitCostEdge import hkaiDirectedGraphExplicitCostEdge
from .hkaiStreamingSet import hkaiStreamingSet


class Constants(Enum):
    INVALID_NODE_INDEX = 4294967295
    INVALID_EDGE_INDEX = 4294967295
    INVALID_VERTEX_INDEX = 4294967295


class EdgeBits(Enum):
    EDGE_IS_USER = 2
    EDGE_EXTERNAL_OPPOSITE = 64


class hkaiDirectedGraphExplicitCost(hkReferencedObject):
    positions: any
    nodes: hkaiDirectedGraphExplicitCostNode
    edges: hkaiDirectedGraphExplicitCostEdge
    nodeData: any
    edgeData: any
    nodeDataStriding: int
    edgeDataStriding: int
    streamingSets: hkaiStreamingSet
