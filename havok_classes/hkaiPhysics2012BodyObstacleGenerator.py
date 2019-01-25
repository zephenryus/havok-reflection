from .hkaiObstacleGenerator import hkaiObstacleGenerator
import struct
from .hkpRigidBody import hkpRigidBody
from .common import any


class hkaiPhysics2012BodyObstacleGenerator(hkaiObstacleGenerator):
    velocityThreshold: float
    rigidBody: hkpRigidBody
    physicsWorldListener: any

    def __init__(self, infile):
        self.velocityThreshold = struct.unpack('>f', infile.read(4))
        self.rigidBody = hkpRigidBody(infile)  # TYPE_POINTER
        self.physicsWorldListener = any(infile)  # TYPE_POINTER
