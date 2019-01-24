from .hkpSphereRepShape import hkpSphereRepShape
from .common import vector4


class hkpMultiSphereShape(hkpSphereRepShape):
    numSpheres: int
    spheres: vector4
