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
        self.frictionCircleYtab = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.xStep = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.xStart = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.wheelSurfaceInertia = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.wheelSurfaceInertiaInv = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.wheelChassisMassRatio = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.wheelRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.wheelRadiusInv = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.wheelDownForceFactor = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.wheelDownForceSumFactor = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} frictionCircleYtab={frictionCircleYtab}, xStep={xStep}, xStart={xStart}, wheelSurfaceInertia={wheelSurfaceInertia}, wheelSurfaceInertiaInv={wheelSurfaceInertiaInv}, wheelChassisMassRatio={wheelChassisMassRatio}, wheelRadius={wheelRadius}, wheelRadiusInv={wheelRadiusInv}, wheelDownForceFactor={wheelDownForceFactor}, wheelDownForceSumFactor={wheelDownForceSumFactor}>".format(**{
            "class_name": self.__class__.__name__,
            "frictionCircleYtab": self.frictionCircleYtab,
            "xStep": self.xStep,
            "xStart": self.xStart,
            "wheelSurfaceInertia": self.wheelSurfaceInertia,
            "wheelSurfaceInertiaInv": self.wheelSurfaceInertiaInv,
            "wheelChassisMassRatio": self.wheelChassisMassRatio,
            "wheelRadius": self.wheelRadius,
            "wheelRadiusInv": self.wheelRadiusInv,
            "wheelDownForceFactor": self.wheelDownForceFactor,
            "wheelDownForceSumFactor": self.wheelDownForceSumFactor,
        })
