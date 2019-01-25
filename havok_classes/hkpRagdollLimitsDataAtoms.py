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
        self.rotations = hkpSetLocalRotationsConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.twistLimit = hkpTwistLimitConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.coneLimit = hkpConeLimitConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.planesLimit = hkpConeLimitConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} rotations={rotations}, twistLimit={twistLimit}, coneLimit={coneLimit}, planesLimit={planesLimit}>".format(**{
            "class_name": self.__class__.__name__,
            "rotations": self.rotations,
            "twistLimit": self.twistLimit,
            "coneLimit": self.coneLimit,
            "planesLimit": self.planesLimit,
        })
