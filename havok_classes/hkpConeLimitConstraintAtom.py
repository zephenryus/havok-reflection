from .hkpConstraintAtom import hkpConstraintAtom
from enum import Enum
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
