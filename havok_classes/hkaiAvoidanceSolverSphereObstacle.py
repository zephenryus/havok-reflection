from .hkSphere import hkSphere
from .common import vector4
import struct


class hkaiAvoidanceSolverSphereObstacle(object):
    sphere: hkSphere
    velocity: vector4

    def __init__(self, infile):
        self.sphere = hkSphere(infile)  # TYPE_STRUCT
        self.velocity = struct.unpack('>4f', infile.read(16))
