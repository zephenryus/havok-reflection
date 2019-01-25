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
        self.spinVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.sumVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.numWheels = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.wheelsSolved = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.stepsSolved = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.invInertia = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.inertia = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.impulseScaling = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.impulseMax = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.isFixed = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.numWheelsOnGround = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} spinVelocity={spinVelocity}, sumVelocity={sumVelocity}, numWheels={numWheels}, wheelsSolved={wheelsSolved}, stepsSolved={stepsSolved}, invInertia={invInertia}, inertia={inertia}, impulseScaling={impulseScaling}, impulseMax={impulseMax}, isFixed={isFixed}, numWheelsOnGround={numWheelsOnGround}>".format(**{
            "class_name": self.__class__.__name__,
            "spinVelocity": self.spinVelocity,
            "sumVelocity": self.sumVelocity,
            "numWheels": self.numWheels,
            "wheelsSolved": self.wheelsSolved,
            "stepsSolved": self.stepsSolved,
            "invInertia": self.invInertia,
            "inertia": self.inertia,
            "impulseScaling": self.impulseScaling,
            "impulseMax": self.impulseMax,
            "isFixed": self.isFixed,
            "numWheelsOnGround": self.numWheelsOnGround,
        })
