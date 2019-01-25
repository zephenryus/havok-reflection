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

    def __init__(self, infile):
        self.rotations = hkpSetLocalRotationsConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.angLimit = hkpAngLimitConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.2dAng = hkp2dAngConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} rotations={rotations}, angLimit={angLimit}, 2dAng={2dAng}>".format(**{
            "class_name": self.__class__.__name__,
            "rotations": self.rotations,
            "angLimit": self.angLimit,
            "2dAng": self.2dAng,
        })
