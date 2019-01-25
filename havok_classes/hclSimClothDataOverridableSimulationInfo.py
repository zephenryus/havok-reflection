from .common import vector4
import struct


class hclSimClothDataOverridableSimulationInfo(object):
    gravity: vector4
    globalDampingPerSecond: float
    collisionTolerance: float
    subSteps: int
    pinchDetectionEnabled: bool
    landscapeCollisionEnabled: bool
    transferMotionEnabled: bool

    def __init__(self, infile):
        self.gravity = struct.unpack('>4f', infile.read(16))
        self.globalDampingPerSecond = struct.unpack('>f', infile.read(4))
        self.collisionTolerance = struct.unpack('>f', infile.read(4))
        self.subSteps = struct.unpack('>I', infile.read(4))
        self.pinchDetectionEnabled = struct.unpack('>?', infile.read(1))
        self.landscapeCollisionEnabled = struct.unpack('>?', infile.read(1))
        self.transferMotionEnabled = struct.unpack('>?', infile.read(1))
