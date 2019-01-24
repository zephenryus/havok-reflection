from enum import Enum
from .hkpSetLocalRotationsConstraintAtom import hkpSetLocalRotationsConstraintAtom
from .hkpTwistLimitConstraintAtom import hkpTwistLimitConstraintAtom
from .hkpConeLimitConstraintAtom import hkpConeLimitConstraintAtom


class Axis(Enum):
    AXIS_TWIST = 0
    AXIS_PLANES = 1
    AXIS_CROSS_PRODUCT = 2


class hkpRagdollLimitsDataAtoms(object):
    rotations: hkpSetLocalRotationsConstraintAtom
    twistLimit: hkpTwistLimitConstraintAtom
    coneLimit: hkpConeLimitConstraintAtom
    planesLimit: hkpConeLimitConstraintAtom
