import struct


class hclSimClothDataLandscapeCollisionData(object):
    landscapeRadius: float
    enableStuckParticleDetection: bool
    stuckParticlesStretchFactorSq: float
    pinchDetectionEnabled: bool
    pinchDetectionPriority: int
    pinchDetectionRadius: float

    def __init__(self, infile):
        self.landscapeRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.enableStuckParticleDetection = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.stuckParticlesStretchFactorSq = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.pinchDetectionEnabled = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.pinchDetectionPriority = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.pinchDetectionRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} landscapeRadius={landscapeRadius}, enableStuckParticleDetection={enableStuckParticleDetection}, stuckParticlesStretchFactorSq={stuckParticlesStretchFactorSq}, pinchDetectionEnabled={pinchDetectionEnabled}, pinchDetectionPriority={pinchDetectionPriority}, pinchDetectionRadius={pinchDetectionRadius}>".format(**{
            "class_name": self.__class__.__name__,
            "landscapeRadius": self.landscapeRadius,
            "enableStuckParticleDetection": self.enableStuckParticleDetection,
            "stuckParticlesStretchFactorSq": self.stuckParticlesStretchFactorSq,
            "pinchDetectionEnabled": self.pinchDetectionEnabled,
            "pinchDetectionPriority": self.pinchDetectionPriority,
            "pinchDetectionRadius": self.pinchDetectionRadius,
        })
