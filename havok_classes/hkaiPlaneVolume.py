from .hkaiVolume import hkaiVolume
from .common import any
from .hkGeometry import hkGeometry
from .hkAabb import hkAabb


class hkaiPlaneVolume(hkaiVolume):
    planes: any
    geometry: hkGeometry
    isInverted: bool
    aabb: hkAabb
