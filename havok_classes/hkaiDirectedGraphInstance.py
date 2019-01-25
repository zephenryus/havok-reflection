from .hkReferencedObject import hkReferencedObject
import struct
from .hkaiDirectedGraphExplicitCost import hkaiDirectedGraphExplicitCost
from typing import List
from .common import get_array
from .hkaiDirectedGraphExplicitCostNode import hkaiDirectedGraphExplicitCostNode
from .hkaiDirectedGraphExplicitCostEdge import hkaiDirectedGraphExplicitCostEdge
from .hkaiDirectedGraphInstanceFreeBlockList import hkaiDirectedGraphInstanceFreeBlockList


class hkaiDirectedGraphInstance(hkReferencedObject):
    originalNodes: any
    originalEdges: any
    originalPositions: any
    originalNodeData: any
    nodeDataStriding: int
    originalEdgeData: any
    edgeDataStriding: int
    sectionUid: int
    runtimeId: int
    originalGraph: any
    nodeMap: List[int]
    instancedNodes: List[hkaiDirectedGraphExplicitCostNode]
    ownedEdges: List[hkaiDirectedGraphExplicitCostEdge]
    ownedEdgeData: List[int]
    userEdgeCount: List[int]
    freeEdgeBlocks: List[hkaiDirectedGraphInstanceFreeBlockList]
    transform: any

    def __init__(self, infile):
        self.originalNodes = any(infile)  # TYPE_SIMPLEARRAY:TYPE_VOID
        self.originalEdges = any(infile)  # TYPE_SIMPLEARRAY:TYPE_VOID
        self.originalPositions = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.originalNodeData = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.nodeDataStriding = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.originalEdgeData = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.edgeDataStriding = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.sectionUid = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.runtimeId = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.originalGraph = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.nodeMap = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32
        self.instancedNodes = get_array(infile, hkaiDirectedGraphExplicitCostNode, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.ownedEdges = get_array(infile, hkaiDirectedGraphExplicitCostEdge, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.ownedEdgeData = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.userEdgeCount = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32
        self.freeEdgeBlocks = get_array(infile, hkaiDirectedGraphInstanceFreeBlockList, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.transform = any(infile)  # TYPE_TRANSFORM:TYPE_VOID

    def __repr__(self):
        return "<{class_name} originalNodes={originalNodes}, originalEdges={originalEdges}, originalPositions={originalPositions}, originalNodeData={originalNodeData}, nodeDataStriding={nodeDataStriding}, originalEdgeData={originalEdgeData}, edgeDataStriding={edgeDataStriding}, sectionUid={sectionUid}, runtimeId={runtimeId}, originalGraph={originalGraph}, nodeMap=[{nodeMap}], instancedNodes=[{instancedNodes}], ownedEdges=[{ownedEdges}], ownedEdgeData=[{ownedEdgeData}], userEdgeCount=[{userEdgeCount}], freeEdgeBlocks=[{freeEdgeBlocks}], transform={transform}>".format(**{
            "class_name": self.__class__.__name__,
            "originalNodes": self.originalNodes,
            "originalEdges": self.originalEdges,
            "originalPositions": self.originalPositions,
            "originalNodeData": self.originalNodeData,
            "nodeDataStriding": self.nodeDataStriding,
            "originalEdgeData": self.originalEdgeData,
            "edgeDataStriding": self.edgeDataStriding,
            "sectionUid": self.sectionUid,
            "runtimeId": self.runtimeId,
            "originalGraph": self.originalGraph,
            "nodeMap": self.nodeMap,
            "instancedNodes": self.instancedNodes,
            "ownedEdges": self.ownedEdges,
            "ownedEdgeData": self.ownedEdgeData,
            "userEdgeCount": self.userEdgeCount,
            "freeEdgeBlocks": self.freeEdgeBlocks,
            "transform": self.transform,
        })
