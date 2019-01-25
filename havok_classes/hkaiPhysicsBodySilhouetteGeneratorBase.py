from .hkaiPointCloudSilhouetteGenerator import hkaiPointCloudSilhouetteGenerator
from .common import vector4
import struct


class hkaiPhysicsBodySilhouetteGeneratorBase(hkaiPointCloudSilhouetteGenerator):
    linearVelocityAndThreshold: vector4

    def __init__(self, infile):
        self.linearVelocityAndThreshold = struct.unpack('>4f', infile.read(16))
