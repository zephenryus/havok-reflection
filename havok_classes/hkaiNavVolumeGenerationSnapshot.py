from .hkGeometry import hkGeometry
from .hkaiNavVolumeGenerationSettings import hkaiNavVolumeGenerationSettings


class hkaiNavVolumeGenerationSnapshot(object):
    geometry: hkGeometry
    settings: hkaiNavVolumeGenerationSettings

    def __init__(self, infile):
        self.geometry = hkGeometry(infile)  # TYPE_STRUCT
        self.settings = hkaiNavVolumeGenerationSettings(infile)  # TYPE_STRUCT
