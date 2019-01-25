from .hkpShape import hkpShape
from typing import List
from .common import get_array
from .hkpMultiRayShapeRay import hkpMultiRayShapeRay
import struct


class hkpMultiRayShape(hkpShape):
    rays: List[hkpMultiRayShapeRay]
    rayPenetrationDistance: float

    def __init__(self, infile):
        self.rays = get_array(infile, hkpMultiRayShapeRay, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.rayPenetrationDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} rays=[{rays}], rayPenetrationDistance={rayPenetrationDistance}>".format(**{
            "class_name": self.__class__.__name__,
            "rays": self.rays,
            "rayPenetrationDistance": self.rayPenetrationDistance,
        })
