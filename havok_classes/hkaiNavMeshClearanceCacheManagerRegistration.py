from .hkaiAstarEdgeFilter import hkaiAstarEdgeFilter


class hkaiNavMeshClearanceCacheManagerRegistration(object):
    id: int
    info: int
    infoMask: int
    cacheIdentifier: int
    filter: hkaiAstarEdgeFilter
