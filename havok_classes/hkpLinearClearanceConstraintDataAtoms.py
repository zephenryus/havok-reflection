from enum import Enum
from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpLinMotorConstraintAtom import hkpLinMotorConstraintAtom
from .hkpLinFrictionConstraintAtom import hkpLinFrictionConstraintAtom
from .hkpAngConstraintAtom import hkpAngConstraintAtom
from .hkpLinLimitConstraintAtom import hkpLinLimitConstraintAtom


class Axis(Enum):
    AXIS_SHAFT = 0
    AXIS_PERP_TO_SHAFT = 1


class hkpLinearClearanceConstraintDataAtoms(object):
    transforms: hkpSetLocalTransformsConstraintAtom
    motor: hkpLinMotorConstraintAtom
    friction0: hkpLinFrictionConstraintAtom
    friction1: hkpLinFrictionConstraintAtom
    friction2: hkpLinFrictionConstraintAtom
    ang: hkpAngConstraintAtom
    linLimit0: hkpLinLimitConstraintAtom
    linLimit1: hkpLinLimitConstraintAtom
    linLimit2: hkpLinLimitConstraintAtom
