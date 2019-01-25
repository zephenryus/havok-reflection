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
        self.gravity = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.globalDampingPerSecond = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.collisionTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.subSteps = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.pinchDetectionEnabled = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.landscapeCollisionEnabled = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.transferMotionEnabled = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} gravity={gravity}, globalDampingPerSecond={globalDampingPerSecond}, collisionTolerance={collisionTolerance}, subSteps={subSteps}, pinchDetectionEnabled={pinchDetectionEnabled}, landscapeCollisionEnabled={landscapeCollisionEnabled}, transferMotionEnabled={transferMotionEnabled}>".format(**{
            "class_name": self.__class__.__name__,
            "gravity": self.gravity,
            "globalDampingPerSecond": self.globalDampingPerSecond,
            "collisionTolerance": self.collisionTolerance,
            "subSteps": self.subSteps,
            "pinchDetectionEnabled": self.pinchDetectionEnabled,
            "landscapeCollisionEnabled": self.landscapeCollisionEnabled,
            "transferMotionEnabled": self.transferMotionEnabled,
        })
