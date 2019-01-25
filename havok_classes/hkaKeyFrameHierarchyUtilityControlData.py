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
        self.hierarchyGain = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.velocityDamping = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.accelerationGain = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.velocityGain = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.positionGain = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.positionMaxLinearVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.positionMaxAngularVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.snapGain = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.snapMaxLinearVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.snapMaxAngularVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.snapMaxLinearDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.snapMaxAngularDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} hierarchyGain={hierarchyGain}, velocityDamping={velocityDamping}, accelerationGain={accelerationGain}, velocityGain={velocityGain}, positionGain={positionGain}, positionMaxLinearVelocity={positionMaxLinearVelocity}, positionMaxAngularVelocity={positionMaxAngularVelocity}, snapGain={snapGain}, snapMaxLinearVelocity={snapMaxLinearVelocity}, snapMaxAngularVelocity={snapMaxAngularVelocity}, snapMaxLinearDistance={snapMaxLinearDistance}, snapMaxAngularDistance={snapMaxAngularDistance}>".format(**{
            "class_name": self.__class__.__name__,
            "hierarchyGain": self.hierarchyGain,
            "velocityDamping": self.velocityDamping,
            "accelerationGain": self.accelerationGain,
            "velocityGain": self.velocityGain,
            "positionGain": self.positionGain,
            "positionMaxLinearVelocity": self.positionMaxLinearVelocity,
            "positionMaxAngularVelocity": self.positionMaxAngularVelocity,
            "snapGain": self.snapGain,
            "snapMaxLinearVelocity": self.snapMaxLinearVelocity,
            "snapMaxAngularVelocity": self.snapMaxAngularVelocity,
            "snapMaxLinearDistance": self.snapMaxLinearDistance,
            "snapMaxAngularDistance": self.snapMaxAngularDistance,
        })
