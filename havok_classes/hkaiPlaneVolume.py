from .hkaiVolume import hkaiVolume
from typing import List
from .common import get_array
from .hkGeometry import hkGeometry
import struct
from .hkAabb import hkAabb


class hkaiPlaneVolume(hkaiVolume):
    planes: List[vector4]
    geometry: hkGeometry
    isInverted: bool
    aabb: hkAabb

    def __init__(self, infile):
        self.planes = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.geometry = hkGeometry(infile)  # TYPE_STRUCT:TYPE_VOID
        self.isInverted = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.aabb = hkAabb(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} planes=[{planes}], geometry={geometry}, isInverted={isInverted}, aabb={aabb}>".format(**{
            "class_name": self.__class__.__name__,
            "planes": self.planes,
            "geometry": self.geometry,
            "isInverted": self.isInverted,
            "aabb": self.aabb,
        })
