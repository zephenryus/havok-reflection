from .hkaiNavMeshQueryMediator import hkaiNavMeshQueryMediator
from .hkaiStreamingCollection import hkaiStreamingCollection
from .hkcdDynamicAabbTree import hkcdDynamicAabbTree
from .hkaiNavMeshCutter import hkaiNavMeshCutter


class hkaiDynamicNavMeshQueryMediator(hkaiNavMeshQueryMediator):
    collection: hkaiStreamingCollection
    aabbTree: hkcdDynamicAabbTree
    cutter: hkaiNavMeshCutter
    cutAabbTolerance: float
