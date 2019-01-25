from .hkpSphereRepShape import hkpSphereRepShape
import struct


class hkpMultiSphereShape(hkpSphereRepShape):
    numSpheres: int
    spheres: vector4

    def __init__(self, infile):
        self.numSpheres = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.spheres = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} numSpheres={numSpheres}, spheres={spheres}>".format(**{
            "class_name": self.__class__.__name__,
            "numSpheres": self.numSpheres,
            "spheres": self.spheres,
        })
