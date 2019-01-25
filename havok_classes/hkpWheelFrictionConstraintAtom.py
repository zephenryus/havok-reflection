from .hkpConstraintAtom import hkpConstraintAtom
import struct
from .hkpWheelFrictionConstraintAtomAxle import hkpWheelFrictionConstraintAtomAxle


class hkpWheelFrictionConstraintAtom(hkpConstraintAtom):
    isEnabled: int
    forwardAxis: int
    sideAxis: int
    radius: float
    axle: hkpWheelFrictionConstraintAtomAxle
    maxFrictionForce: float
    torque: float
    frictionImpulse: float
    slipImpulse: float
    padding: int

    def __init__(self, infile):
        self.isEnabled = struct.unpack('>B', infile.read(1))
        self.forwardAxis = struct.unpack('>B', infile.read(1))
        self.sideAxis = struct.unpack('>B', infile.read(1))
        self.radius = struct.unpack('>f', infile.read(4))
        self.axle = hkpWheelFrictionConstraintAtomAxle(infile)  # TYPE_POINTER
        self.maxFrictionForce = struct.unpack('>f', infile.read(4))
        self.torque = struct.unpack('>f', infile.read(4))
        self.frictionImpulse = struct.unpack('>f', infile.read(4))
        self.slipImpulse = struct.unpack('>f', infile.read(4))
        self.padding = struct.unpack('>B', infile.read(1))
