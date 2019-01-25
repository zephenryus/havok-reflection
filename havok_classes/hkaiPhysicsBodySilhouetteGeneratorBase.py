from .hkaiPointCloudSilhouetteGenerator import hkaiPointCloudSilhouetteGenerator
import struct


class hkaiPhysicsBodySilhouetteGeneratorBase(hkaiPointCloudSilhouetteGenerator):
    linearVelocityAndThreshold: vector4

    def __init__(self, infile):
        self.linearVelocityAndThreshold = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} linearVelocityAndThreshold={linearVelocityAndThreshold}>".format(**{
            "class_name": self.__class__.__name__,
            "linearVelocityAndThreshold": self.linearVelocityAndThreshold,
        })
