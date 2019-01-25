from .hkReferencedObject import hkReferencedObject
from .common import any
import struct
from .hkaiDirectedGraphExplicitCost import hkaiDirectedGraphExplicitCost
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
    originalGraph: hkaiDirectedGraphExplicitCost
    nodeMap: any
    instancedNodes: hkaiDirectedGraphExplicitCostNode
    ownedEdges: hkaiDirectedGraphExplicitCostEdge
    ownedEdgeData: any
    userEdgeCount: any
    freeEdgeBlocks: hkaiDirectedGraphInstanceFreeBlockList
    transform: any

    def __init__(self, infile):
        self.originalNodes = any(infile)  # TYPE_SIMPLEARRAY
        self.originalEdges = any(infile)  # TYPE_SIMPLEARRAY
        self.originalPositions = any(infile)  # TYPE_POINTER
        self.originalNodeData = any(infile)  # TYPE_POINTER
        self.nodeDataStriding = struct.unpack('>i', infile.read(4))
        self.originalEdgeData = any(infile)  # TYPE_POINTER
        self.edgeDataStriding = struct.unpack('>i', infile.read(4))
        self.sectionUid = struct.unpack('>I', infile.read(4))
        self.runtimeId = struct.unpack('>i', infile.read(4))
        self.originalGraph = hkaiDirectedGraphExplicitCost(infile)  # TYPE_POINTER
        self.nodeMap = any(infile)  # TYPE_ARRAY
        self.instancedNodes = hkaiDirectedGraphExplicitCostNode(infile)  # TYPE_ARRAY
        self.ownedEdges = hkaiDirectedGraphExplicitCostEdge(infile)  # TYPE_ARRAY
        self.ownedEdgeData = any(infile)  # TYPE_ARRAY
        self.userEdgeCount = any(infile)  # TYPE_ARRAY
        self.freeEdgeBlocks = hkaiDirectedGraphInstanceFreeBlockList(infile)  # TYPE_ARRAY
        self.transform = any(infile)  # TYPE_TRANSFORM
