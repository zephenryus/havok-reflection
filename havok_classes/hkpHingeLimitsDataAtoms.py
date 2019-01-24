from enum import Enum
from .hkpSetLocalRotationsConstraintAtom import hkpSetLocalRotationsConstraintAtom
from .hkpAngLimitConstraintAtom import hkpAngLimitConstraintAtom
from .hkp2dAngConstraintAtom import hkp2dAngConstraintAtom


class Axis(Enum):
    AXIS_AXLE = 0
    AXIS_PERP_TO_AXLE_1 = 1
    AXIS_PERP_TO_AXLE_2 = 2


class hkpHingeLimitsDataAtoms(object):
    rotations: hkpSetLocalRotationsConstraintAtom
    angLimit: hkpAngLimitConstraintAtom
    2dAng: hkp2dAngConstraintAtom
