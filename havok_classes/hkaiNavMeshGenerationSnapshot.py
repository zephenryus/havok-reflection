from .hkGeometry import hkGeometry
from .hkaiNavMeshGenerationSettings import hkaiNavMeshGenerationSettings


class hkaiNavMeshGenerationSnapshot(object):
    geometry: hkGeometry
    settings: hkaiNavMeshGenerationSettings

    def __init__(self, infile):
        self.geometry = hkGeometry(infile)  # TYPE_STRUCT:TYPE_VOID
        self.settings = hkaiNavMeshGenerationSettings(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} geometry={geometry}, settings={settings}>".format(**{
            "class_name": self.__class__.__name__,
            "geometry": self.geometry,
            "settings": self.settings,
        })
