from enum import Enum
from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpLinLimitConstraintAtom import hkpLinLimitConstraintAtom
from .hkpLinSoftConstraintAtom import hkpLinSoftConstraintAtom
from .hkpLinConstraintAtom import hkpLinConstraintAtom
from .hkpSetLocalRotationsConstraintAtom import hkpSetLocalRotationsConstraintAtom
from .hkp2dAngConstraintAtom import hkp2dAngConstraintAtom


class Axis(Enum):
    AXIS_SUSPENSION = 0
    AXIS_PERP_SUSPENSION = 1
    AXIS_AXLE = 0
    AXIS_STEERING = 1


class hkpWheelConstraintDataAtoms(object):
    suspensionBase: hkpSetLocalTransformsConstraintAtom
    lin0Limit: hkpLinLimitConstraintAtom
    lin0Soft: hkpLinSoftConstraintAtom
    lin1: hkpLinConstraintAtom
    lin2: hkpLinConstraintAtom
    steeringBase: hkpSetLocalRotationsConstraintAtom
    2dAng: hkp2dAngConstraintAtom

    def __init__(self, infile):
        self.suspensionBase = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.lin0Limit = hkpLinLimitConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.lin0Soft = hkpLinSoftConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.lin1 = hkpLinConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.lin2 = hkpLinConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.steeringBase = hkpSetLocalRotationsConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.2dAng = hkp2dAngConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} suspensionBase={suspensionBase}, lin0Limit={lin0Limit}, lin0Soft={lin0Soft}, lin1={lin1}, lin2={lin2}, steeringBase={steeringBase}, 2dAng={2dAng}>".format(**{
            "class_name": self.__class__.__name__,
            "suspensionBase": self.suspensionBase,
            "lin0Limit": self.lin0Limit,
            "lin0Soft": self.lin0Soft,
            "lin1": self.lin1,
            "lin2": self.lin2,
            "steeringBase": self.steeringBase,
            "2dAng": self.2dAng,
        })
