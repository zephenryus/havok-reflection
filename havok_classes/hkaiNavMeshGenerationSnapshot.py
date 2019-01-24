from .hkGeometry import hkGeometry
from .hkaiNavMeshGenerationSettings import hkaiNavMeshGenerationSettings


class hkaiNavMeshGenerationSnapshot(object):
    geometry: hkGeometry
    settings: hkaiNavMeshGenerationSettings
