import struct


class hkpVehicleFrictionDescriptionAxisDescription(object):
    frictionCircleYtab: float
    xStep: float
    xStart: float
    wheelSurfaceInertia: float
    wheelSurfaceInertiaInv: float
    wheelChassisMassRatio: float
    wheelRadius: float
    wheelRadiusInv: float
    wheelDownForceFactor: float
    wheelDownForceSumFactor: float

    def __init__(self, infile):
        self.frictionCircleYtab = struct.unpack('>f', infile.read(4))
        self.xStep = struct.unpack('>f', infile.read(4))
        self.xStart = struct.unpack('>f', infile.read(4))
        self.wheelSurfaceInertia = struct.unpack('>f', infile.read(4))
        self.wheelSurfaceInertiaInv = struct.unpack('>f', infile.read(4))
        self.wheelChassisMassRatio = struct.unpack('>f', infile.read(4))
        self.wheelRadius = struct.unpack('>f', infile.read(4))
        self.wheelRadiusInv = struct.unpack('>f', infile.read(4))
        self.wheelDownForceFactor = struct.unpack('>f', infile.read(4))
        self.wheelDownForceSumFactor = struct.unpack('>f', infile.read(4))
