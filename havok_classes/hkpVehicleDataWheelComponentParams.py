import struct


class hkpVehicleDataWheelComponentParams(object):
    radius: float
    mass: float
    width: float
    friction: float
    viscosityFriction: float
    maxFriction: float
    slipAngle: float
    forceFeedbackMultiplier: float
    maxContactBodyAcceleration: float
    axle: int

    def __init__(self, infile):
        self.radius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.mass = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.width = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.friction = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.viscosityFriction = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxFriction = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.slipAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.forceFeedbackMultiplier = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxContactBodyAcceleration = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.axle = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} radius={radius}, mass={mass}, width={width}, friction={friction}, viscosityFriction={viscosityFriction}, maxFriction={maxFriction}, slipAngle={slipAngle}, forceFeedbackMultiplier={forceFeedbackMultiplier}, maxContactBodyAcceleration={maxContactBodyAcceleration}, axle={axle}>".format(**{
            "class_name": self.__class__.__name__,
            "radius": self.radius,
            "mass": self.mass,
            "width": self.width,
            "friction": self.friction,
            "viscosityFriction": self.viscosityFriction,
            "maxFriction": self.maxFriction,
            "slipAngle": self.slipAngle,
            "forceFeedbackMultiplier": self.forceFeedbackMultiplier,
            "maxContactBodyAcceleration": self.maxContactBodyAcceleration,
            "axle": self.axle,
        })
