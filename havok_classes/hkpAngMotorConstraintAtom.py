from .hkpConstraintAtom import hkpConstraintAtom
import struct
from .hkpConstraintMotor import hkpConstraintMotor


class hkpAngMotorConstraintAtom(hkpConstraintAtom):
    isEnabled: bool
    motorAxis: int
    initializedOffset: int
    previousTargetAngleOffset: int
    motor: hkpConstraintMotor
    targetAngle: float
    correspondingAngLimitSolverResultOffset: int
    padding: int

    def __init__(self, infile):
        self.isEnabled = struct.unpack('>?', infile.read(1))
        self.motorAxis = struct.unpack('>B', infile.read(1))
        self.initializedOffset = struct.unpack('>h', infile.read(2))
        self.previousTargetAngleOffset = struct.unpack('>h', infile.read(2))
        self.motor = hkpConstraintMotor(infile)  # TYPE_POINTER
        self.targetAngle = struct.unpack('>f', infile.read(4))
        self.correspondingAngLimitSolverResultOffset = struct.unpack('>h', infile.read(2))
        self.padding = struct.unpack('>B', infile.read(1))
