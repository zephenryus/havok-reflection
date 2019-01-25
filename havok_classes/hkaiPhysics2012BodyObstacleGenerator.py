from .hkaiObstacleGenerator import hkaiObstacleGenerator
import struct
from .hkpRigidBody import hkpRigidBody


class hkaiPhysics2012BodyObstacleGenerator(hkaiObstacleGenerator):
    velocityThreshold: float
    rigidBody: any
    physicsWorldListener: any

    def __init__(self, infile):
        self.velocityThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.rigidBody = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.physicsWorldListener = any(infile)  # TYPE_POINTER:TYPE_VOID

    def __repr__(self):
        return "<{class_name} velocityThreshold={velocityThreshold}, rigidBody={rigidBody}, physicsWorldListener={physicsWorldListener}>".format(**{
            "class_name": self.__class__.__name__,
            "velocityThreshold": self.velocityThreshold,
            "rigidBody": self.rigidBody,
            "physicsWorldListener": self.physicsWorldListener,
        })
