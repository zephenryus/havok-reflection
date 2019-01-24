from .hkpConstraintData import hkpConstraintData
from enum import Enum
from .hkp6DofConstraintDataBlueprints import hkp6DofConstraintDataBlueprints
from .common import any


class MotorIndex(Enum):
    MOTOR_TWIST = 0
    MOTOR_SWING0 = 1
    MOTOR_SWING1 = 2
    MOTOR_ALL = 3


class Axis(Enum):
    AXIS_TWIST = 0
    AXIS_SWING0 = 1
    AXIS_SWING1 = 2


class hkp6DofConstraintData(hkpConstraintData):
    blueprints: hkp6DofConstraintDataBlueprints
    isDirty: bool
    numRuntimeElements: int
    atomToCompiledAtomOffset: int
    resultToRuntime: int
    compiledAtoms: any
