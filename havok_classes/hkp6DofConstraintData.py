from .hkpConstraintData import hkpConstraintData
from enum import Enum
from .hkp6DofConstraintDataBlueprints import hkp6DofConstraintDataBlueprints
import struct
from typing import List
from .common import get_array


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
    compiledAtoms: List[any]

    def __init__(self, infile):
        self.blueprints = hkp6DofConstraintDataBlueprints(infile)  # TYPE_STRUCT:TYPE_VOID
        self.isDirty = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.numRuntimeElements = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.atomToCompiledAtomOffset = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.resultToRuntime = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.compiledAtoms = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_VOID

    def __repr__(self):
        return "<{class_name} blueprints={blueprints}, isDirty={isDirty}, numRuntimeElements={numRuntimeElements}, atomToCompiledAtomOffset={atomToCompiledAtomOffset}, resultToRuntime={resultToRuntime}, compiledAtoms=[{compiledAtoms}]>".format(**{
            "class_name": self.__class__.__name__,
            "blueprints": self.blueprints,
            "isDirty": self.isDirty,
            "numRuntimeElements": self.numRuntimeElements,
            "atomToCompiledAtomOffset": self.atomToCompiledAtomOffset,
            "resultToRuntime": self.resultToRuntime,
            "compiledAtoms": self.compiledAtoms,
        })
