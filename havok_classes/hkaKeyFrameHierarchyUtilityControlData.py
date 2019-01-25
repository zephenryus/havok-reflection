import struct


class hkaKeyFrameHierarchyUtilityControlData(object):
    hierarchyGain: float
    velocityDamping: float
    accelerationGain: float
    velocityGain: float
    positionGain: float
    positionMaxLinearVelocity: float
    positionMaxAngularVelocity: float
    snapGain: float
    snapMaxLinearVelocity: float
    snapMaxAngularVelocity: float
    snapMaxLinearDistance: float
    snapMaxAngularDistance: float

    def __init__(self, infile):
        self.hierarchyGain = struct.unpack('>f', infile.read(4))
        self.velocityDamping = struct.unpack('>f', infile.read(4))
        self.accelerationGain = struct.unpack('>f', infile.read(4))
        self.velocityGain = struct.unpack('>f', infile.read(4))
        self.positionGain = struct.unpack('>f', infile.read(4))
        self.positionMaxLinearVelocity = struct.unpack('>f', infile.read(4))
        self.positionMaxAngularVelocity = struct.unpack('>f', infile.read(4))
        self.snapGain = struct.unpack('>f', infile.read(4))
        self.snapMaxLinearVelocity = struct.unpack('>f', infile.read(4))
        self.snapMaxAngularVelocity = struct.unpack('>f', infile.read(4))
        self.snapMaxLinearDistance = struct.unpack('>f', infile.read(4))
        self.snapMaxAngularDistance = struct.unpack('>f', infile.read(4))
