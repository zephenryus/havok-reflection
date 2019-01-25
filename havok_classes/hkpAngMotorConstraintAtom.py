from .hkpConstraintAtom import hkpConstraintAtom
import struct
from .hkpConstraintMotor import hkpConstraintMotor


class hkpAngMotorConstraintAtom(hkpConstraintAtom):
    isEnabled: bool
    motorAxis: int
    initializedOffset: int
    previousTargetAngleOffset: int
    motor: any
    targetAngle: float
    correspondingAngLimitSolverResultOffset: int
    padding: int

    def __init__(self, infile):
        self.isEnabled = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.motorAxis = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.initializedOffset = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.previousTargetAngleOffset = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.motor = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.targetAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.correspondingAngLimitSolverResultOffset = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} isEnabled={isEnabled}, motorAxis={motorAxis}, initializedOffset={initializedOffset}, previousTargetAngleOffset={previousTargetAngleOffset}, motor={motor}, targetAngle={targetAngle}, correspondingAngLimitSolverResultOffset={correspondingAngLimitSolverResultOffset}, padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "isEnabled": self.isEnabled,
            "motorAxis": self.motorAxis,
            "initializedOffset": self.initializedOffset,
            "previousTargetAngleOffset": self.previousTargetAngleOffset,
            "motor": self.motor,
            "targetAngle": self.targetAngle,
            "correspondingAngLimitSolverResultOffset": self.correspondingAngLimitSolverResultOffset,
            "padding": self.padding,
        })
