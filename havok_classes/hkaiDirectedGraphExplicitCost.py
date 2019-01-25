from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .common import any
from .hkaiDirectedGraphExplicitCostNode import hkaiDirectedGraphExplicitCostNode
from .hkaiDirectedGraphExplicitCostEdge import hkaiDirectedGraphExplicitCostEdge
import struct
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

    def __init__(self, infile):
        self.positions = any(infile)  # TYPE_ARRAY
        self.nodes = hkaiDirectedGraphExplicitCostNode(infile)  # TYPE_ARRAY
        self.edges = hkaiDirectedGraphExplicitCostEdge(infile)  # TYPE_ARRAY
        self.nodeData = any(infile)  # TYPE_ARRAY
        self.edgeData = any(infile)  # TYPE_ARRAY
        self.nodeDataStriding = struct.unpack('>i', infile.read(4))
        self.edgeDataStriding = struct.unpack('>i', infile.read(4))
        self.streamingSets = hkaiStreamingSet(infile)  # TYPE_ARRAY
