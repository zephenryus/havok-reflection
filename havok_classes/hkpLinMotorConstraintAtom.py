from .hkpConstraintAtom import hkpConstraintAtom
import struct
from .hkpConstraintMotor import hkpConstraintMotor


class hkpLinMotorConstraintAtom(hkpConstraintAtom):
    isEnabled: bool
    motorAxis: int
    initializedOffset: int
    previousTargetPositionOffset: int
    motor: any
    targetPosition: float
    padding: int

    def __init__(self, infile):
        self.isEnabled = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.motorAxis = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.initializedOffset = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.previousTargetPositionOffset = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.motor = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.targetPosition = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} isEnabled={isEnabled}, motorAxis={motorAxis}, initializedOffset={initializedOffset}, previousTargetPositionOffset={previousTargetPositionOffset}, motor={motor}, targetPosition={targetPosition}, padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "isEnabled": self.isEnabled,
            "motorAxis": self.motorAxis,
            "initializedOffset": self.initializedOffset,
            "previousTargetPositionOffset": self.previousTargetPositionOffset,
            "motor": self.motor,
            "targetPosition": self.targetPosition,
            "padding": self.padding,
        })
