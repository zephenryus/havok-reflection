from .hkpConstraintData import hkpConstraintData
from enum import Enum
from .hkpBridgeAtoms import hkpBridgeAtoms
from .hkpParametricCurve import hkpParametricCurve
from .enums import OrientationConstraintType
from .common import any


class OrientationConstraintType(Enum):
    CONSTRAIN_ORIENTATION_INVALID = 0
    CONSTRAIN_ORIENTATION_NONE = 1
    CONSTRAIN_ORIENTATION_ALLOW_SPIN = 2
    CONSTRAIN_ORIENTATION_TO_PATH = 3
    CONSTRAIN_ORIENTATION_MAX_ID = 4


class hkpPointToPathConstraintData(hkpConstraintData):
    atoms: hkpBridgeAtoms
    path: hkpParametricCurve
    maxFrictionForce: float
    angularConstrainedDOF: OrientationConstraintType
    transform_OS_KS: any
