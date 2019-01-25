from .hkReferencedObject import hkReferencedObject
from enum import Enum
from typing import List
from .common import get_array
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
    positions: List[vector4]
    nodes: List[hkaiDirectedGraphExplicitCostNode]
    edges: List[hkaiDirectedGraphExplicitCostEdge]
    nodeData: List[int]
    edgeData: List[int]
    nodeDataStriding: int
    edgeDataStriding: int
    streamingSets: List[hkaiStreamingSet]

    def __init__(self, infile):
        self.positions = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.nodes = get_array(infile, hkaiDirectedGraphExplicitCostNode, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.edges = get_array(infile, hkaiDirectedGraphExplicitCostEdge, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.nodeData = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.edgeData = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.nodeDataStriding = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.edgeDataStriding = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.streamingSets = get_array(infile, hkaiStreamingSet, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} positions=[{positions}], nodes=[{nodes}], edges=[{edges}], nodeData=[{nodeData}], edgeData=[{edgeData}], nodeDataStriding={nodeDataStriding}, edgeDataStriding={edgeDataStriding}, streamingSets=[{streamingSets}]>".format(**{
            "class_name": self.__class__.__name__,
            "positions": self.positions,
            "nodes": self.nodes,
            "edges": self.edges,
            "nodeData": self.nodeData,
            "edgeData": self.edgeData,
            "nodeDataStriding": self.nodeDataStriding,
            "edgeDataStriding": self.edgeDataStriding,
            "streamingSets": self.streamingSets,
        })
