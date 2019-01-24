from .hkReferencedObject import hkReferencedObject
from .common import any
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
