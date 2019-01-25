from .hkSphere import hkSphere
import struct


class hkaiAvoidanceSolverSphereObstacle(object):
    sphere: hkSphere
    velocity: vector4

    def __init__(self, infile):
        self.sphere = hkSphere(infile)  # TYPE_STRUCT:TYPE_VOID
        self.velocity = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} sphere={sphere}, velocity={velocity}>".format(**{
            "class_name": self.__class__.__name__,
            "sphere": self.sphere,
            "velocity": self.velocity,
        })
