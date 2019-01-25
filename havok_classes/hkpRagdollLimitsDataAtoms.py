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

    def __init__(self, infile):
        self.rotations = hkpSetLocalRotationsConstraintAtom(infile)  # TYPE_STRUCT
        self.twistLimit = hkpTwistLimitConstraintAtom(infile)  # TYPE_STRUCT
        self.coneLimit = hkpConeLimitConstraintAtom(infile)  # TYPE_STRUCT
        self.planesLimit = hkpConeLimitConstraintAtom(infile)  # TYPE_STRUCT
