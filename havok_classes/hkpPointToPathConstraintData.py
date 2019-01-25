from .hkpConstraintData import hkpConstraintData
from enum import Enum
from .hkpBridgeAtoms import hkpBridgeAtoms
from .hkpParametricCurve import hkpParametricCurve
import struct
from .enums import OrientationConstraintType


class OrientationConstraintType(Enum):
    CONSTRAIN_ORIENTATION_INVALID = 0
    CONSTRAIN_ORIENTATION_NONE = 1
    CONSTRAIN_ORIENTATION_ALLOW_SPIN = 2
    CONSTRAIN_ORIENTATION_TO_PATH = 3
    CONSTRAIN_ORIENTATION_MAX_ID = 4


class hkpPointToPathConstraintData(hkpConstraintData):
    atoms: hkpBridgeAtoms
    path: any
    maxFrictionForce: float
    angularConstrainedDOF: OrientationConstraintType
    transform_OS_KS: any

    def __init__(self, infile):
        self.atoms = hkpBridgeAtoms(infile)  # TYPE_STRUCT:TYPE_VOID
        self.path = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.maxFrictionForce = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.angularConstrainedDOF = OrientationConstraintType(infile)  # TYPE_ENUM:TYPE_INT8
        self.transform_OS_KS = any(infile)  # TYPE_TRANSFORM:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}, path={path}, maxFrictionForce={maxFrictionForce}, angularConstrainedDOF={angularConstrainedDOF}, transform_OS_KS={transform_OS_KS}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
            "path": self.path,
            "maxFrictionForce": self.maxFrictionForce,
            "angularConstrainedDOF": self.angularConstrainedDOF,
            "transform_OS_KS": self.transform_OS_KS,
        })
