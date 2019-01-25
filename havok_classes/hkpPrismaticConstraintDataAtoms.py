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

    def __init__(self, infile):
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT
        self.motor = hkpLinMotorConstraintAtom(infile)  # TYPE_STRUCT
        self.friction = hkpLinFrictionConstraintAtom(infile)  # TYPE_STRUCT
        self.ang = hkpAngConstraintAtom(infile)  # TYPE_STRUCT
        self.lin0 = hkpLinConstraintAtom(infile)  # TYPE_STRUCT
        self.lin1 = hkpLinConstraintAtom(infile)  # TYPE_STRUCT
        self.linLimit = hkpLinLimitConstraintAtom(infile)  # TYPE_STRUCT
