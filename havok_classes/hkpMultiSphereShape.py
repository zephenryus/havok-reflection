from .hkpSphereRepShape import hkpSphereRepShape
import struct
from .common import vector4


class hkpMultiSphereShape(hkpSphereRepShape):
    numSpheres: int
    spheres: vector4

    def __init__(self, infile):
        self.numSpheres = struct.unpack('>i', infile.read(4))
        self.spheres = struct.unpack('>4f', infile.read(16))
