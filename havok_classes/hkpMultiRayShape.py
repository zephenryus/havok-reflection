from .hkpShape import hkpShape
from .hkpMultiRayShapeRay import hkpMultiRayShapeRay
import struct


class hkpMultiRayShape(hkpShape):
    rays: hkpMultiRayShapeRay
    rayPenetrationDistance: float

    def __init__(self, infile):
        self.rays = hkpMultiRayShapeRay(infile)  # TYPE_ARRAY
        self.rayPenetrationDistance = struct.unpack('>f', infile.read(4))
