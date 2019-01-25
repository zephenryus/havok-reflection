from .hkpConstraintData import hkpConstraintData
from enum import Enum
from .hkp6DofConstraintDataBlueprints import hkp6DofConstraintDataBlueprints
import struct
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

    def __init__(self, infile):
        self.blueprints = hkp6DofConstraintDataBlueprints(infile)  # TYPE_STRUCT
        self.isDirty = struct.unpack('>?', infile.read(1))
        self.numRuntimeElements = struct.unpack('>i', infile.read(4))
        self.atomToCompiledAtomOffset = struct.unpack('>i', infile.read(4))
        self.resultToRuntime = struct.unpack('>i', infile.read(4))
        self.compiledAtoms = any(infile)  # TYPE_ARRAY
