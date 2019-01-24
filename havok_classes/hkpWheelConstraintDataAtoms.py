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
