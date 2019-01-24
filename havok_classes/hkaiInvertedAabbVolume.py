from .hkaiVolume import hkaiVolume
from .hkAabb import hkAabb
from .hkGeometry import hkGeometry


class hkaiInvertedAabbVolume(hkaiVolume):
    aabb: hkAabb
    geometry: hkGeometry
