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
        self.isEnabled = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.twistAxisInA = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.refAxisInB = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.angleMeasurementMode = MeasurementMode(infile)  # TYPE_ENUM:TYPE_UINT8
        self.memOffsetToAngleOffset = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.minAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.angularLimitsTauFactor = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.angularLimitsDampFactor = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} isEnabled={isEnabled}, twistAxisInA={twistAxisInA}, refAxisInB={refAxisInB}, angleMeasurementMode={angleMeasurementMode}, memOffsetToAngleOffset={memOffsetToAngleOffset}, minAngle={minAngle}, maxAngle={maxAngle}, angularLimitsTauFactor={angularLimitsTauFactor}, angularLimitsDampFactor={angularLimitsDampFactor}, padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "isEnabled": self.isEnabled,
            "twistAxisInA": self.twistAxisInA,
            "refAxisInB": self.refAxisInB,
            "angleMeasurementMode": self.angleMeasurementMode,
            "memOffsetToAngleOffset": self.memOffsetToAngleOffset,
            "minAngle": self.minAngle,
            "maxAngle": self.maxAngle,
            "angularLimitsTauFactor": self.angularLimitsTauFactor,
            "angularLimitsDampFactor": self.angularLimitsDampFactor,
            "padding": self.padding,
        })
