import struct


class hclSimClothDataLandscapeCollisionData(object):
    landscapeRadius: float
    enableStuckParticleDetection: bool
    stuckParticlesStretchFactorSq: float
    pinchDetectionEnabled: bool
    pinchDetectionPriority: int
    pinchDetectionRadius: float

    def __init__(self, infile):
        self.landscapeRadius = struct.unpack('>f', infile.read(4))
        self.enableStuckParticleDetection = struct.unpack('>?', infile.read(1))
        self.stuckParticlesStretchFactorSq = struct.unpack('>f', infile.read(4))
        self.pinchDetectionEnabled = struct.unpack('>?', infile.read(1))
        self.pinchDetectionPriority = struct.unpack('>b', infile.read(1))
        self.pinchDetectionRadius = struct.unpack('>f', infile.read(4))
