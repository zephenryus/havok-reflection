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
        self.radius = struct.unpack('>f', infile.read(4))
        self.mass = struct.unpack('>f', infile.read(4))
        self.width = struct.unpack('>f', infile.read(4))
        self.friction = struct.unpack('>f', infile.read(4))
        self.viscosityFriction = struct.unpack('>f', infile.read(4))
        self.maxFriction = struct.unpack('>f', infile.read(4))
        self.slipAngle = struct.unpack('>f', infile.read(4))
        self.forceFeedbackMultiplier = struct.unpack('>f', infile.read(4))
        self.maxContactBodyAcceleration = struct.unpack('>f', infile.read(4))
        self.axle = struct.unpack('>b', infile.read(1))
