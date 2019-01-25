from .hkpConstraintAtom import hkpConstraintAtom
import struct
from .hkpConstraintMotor import hkpConstraintMotor


class hkpLinMotorConstraintAtom(hkpConstraintAtom):
    isEnabled: bool
    motorAxis: int
    initializedOffset: int
    previousTargetPositionOffset: int
    motor: hkpConstraintMotor
    targetPosition: float
    padding: int

    def __init__(self, infile):
        self.isEnabled = struct.unpack('>?', infile.read(1))
        self.motorAxis = struct.unpack('>B', infile.read(1))
        self.initializedOffset = struct.unpack('>h', infile.read(2))
        self.previousTargetPositionOffset = struct.unpack('>h', infile.read(2))
        self.motor = hkpConstraintMotor(infile)  # TYPE_POINTER
        self.targetPosition = struct.unpack('>f', infile.read(4))
        self.padding = struct.unpack('>B', infile.read(1))
