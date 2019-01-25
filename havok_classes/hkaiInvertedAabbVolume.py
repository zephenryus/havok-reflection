from .hkaiVolume import hkaiVolume
from .hkAabb import hkAabb
from .hkGeometry import hkGeometry


class hkaiInvertedAabbVolume(hkaiVolume):
    aabb: hkAabb
    geometry: hkGeometry

    def __init__(self, infile):
        self.aabb = hkAabb(infile)  # TYPE_STRUCT
        self.geometry = hkGeometry(infile)  # TYPE_STRUCT
