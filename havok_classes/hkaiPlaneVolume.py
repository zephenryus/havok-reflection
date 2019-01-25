from .hkaiVolume import hkaiVolume
from .common import any
from .hkGeometry import hkGeometry
import struct
from .hkAabb import hkAabb


class hkaiPlaneVolume(hkaiVolume):
    planes: any
    geometry: hkGeometry
    isInverted: bool
    aabb: hkAabb

    def __init__(self, infile):
        self.planes = any(infile)  # TYPE_ARRAY
        self.geometry = hkGeometry(infile)  # TYPE_STRUCT
        self.isInverted = struct.unpack('>?', infile.read(1))
        self.aabb = hkAabb(infile)  # TYPE_STRUCT
