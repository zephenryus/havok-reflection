from .hkpConstraintAtom import hkpConstraintAtom
from enum import Enum
import struct
from .enums import MeasurementMode


class MeasurementMode(Enum):
    ZERO_WHEN_VECTORS_ALIGNED = 0
    ZERO_WHEN_VECTORS_PERPENDICULAR = 1


class hkpConeLimitConstraintAtom(hkpConstraintAtom):
    isEnabled: int
    twistAxisInA: int
    refAxisInB: int
    angleMeasurementMode: MeasurementMode
    memOffsetToAngleOffset: int
    minAngle: float
    maxAngle: float
    angularLimitsTauFactor: float
    angularLimitsDampFactor: float
    padding: int

    def __init__(self, infile):
        self.isEnabled = struct.unpack('>B', infile.read(1))
        self.twistAxisInA = struct.unpack('>B', infile.read(1))
        self.refAxisInB = struct.unpack('>B', infile.read(1))
        self.angleMeasurementMode = MeasurementMode(infile)  # TYPE_ENUM
        self.memOffsetToAngleOffset = struct.unpack('>B', infile.read(1))
        self.minAngle = struct.unpack('>f', infile.read(4))
        self.maxAngle = struct.unpack('>f', infile.read(4))
        self.angularLimitsTauFactor = struct.unpack('>f', infile.read(4))
        self.angularLimitsDampFactor = struct.unpack('>f', infile.read(4))
        self.padding = struct.unpack('>B', infile.read(1))
