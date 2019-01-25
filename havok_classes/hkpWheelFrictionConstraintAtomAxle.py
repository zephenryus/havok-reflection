import struct


class hkpWheelFrictionConstraintAtomAxle(object):
    spinVelocity: float
    sumVelocity: float
    numWheels: int
    wheelsSolved: int
    stepsSolved: int
    invInertia: float
    inertia: float
    impulseScaling: float
    impulseMax: float
    isFixed: bool
    numWheelsOnGround: int

    def __init__(self, infile):
        self.spinVelocity = struct.unpack('>f', infile.read(4))
        self.sumVelocity = struct.unpack('>f', infile.read(4))
        self.numWheels = struct.unpack('>i', infile.read(4))
        self.wheelsSolved = struct.unpack('>i', infile.read(4))
        self.stepsSolved = struct.unpack('>i', infile.read(4))
        self.invInertia = struct.unpack('>f', infile.read(4))
        self.inertia = struct.unpack('>f', infile.read(4))
        self.impulseScaling = struct.unpack('>f', infile.read(4))
        self.impulseMax = struct.unpack('>f', infile.read(4))
        self.isFixed = struct.unpack('>?', infile.read(1))
        self.numWheelsOnGround = struct.unpack('>i', infile.read(4))
