from .hkGeometry import hkGeometry
from .hkaiNavMeshGenerationSettings import hkaiNavMeshGenerationSettings


class hkaiNavMeshGenerationSnapshot(object):
    geometry: hkGeometry
    settings: hkaiNavMeshGenerationSettings

    def __init__(self, infile):
        self.geometry = hkGeometry(infile)  # TYPE_STRUCT
        self.settings = hkaiNavMeshGenerationSettings(infile)  # TYPE_STRUCT
