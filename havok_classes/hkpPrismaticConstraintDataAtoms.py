from enum import Enum
from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpLinMotorConstraintAtom import hkpLinMotorConstraintAtom
from .hkpLinFrictionConstraintAtom import hkpLinFrictionConstraintAtom
from .hkpAngConstraintAtom import hkpAngConstraintAtom
from .hkpLinConstraintAtom import hkpLinConstraintAtom
from .hkpLinLimitConstraintAtom import hkpLinLimitConstraintAtom


class Axis(Enum):
    AXIS_SHAFT = 0
    AXIS_PERP_TO_SHAFT = 1


class hkpPrismaticConstraintDataAtoms(object):
    transforms: hkpSetLocalTransformsConstraintAtom
    motor: hkpLinMotorConstraintAtom
    friction: hkpLinFrictionConstraintAtom
    ang: hkpAngConstraintAtom
    lin0: hkpLinConstraintAtom
    lin1: hkpLinConstraintAtom
    linLimit: hkpLinLimitConstraintAtom
