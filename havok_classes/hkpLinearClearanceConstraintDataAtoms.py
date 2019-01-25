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

    def __init__(self, infile):
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.motor = hkpLinMotorConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.friction0 = hkpLinFrictionConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.friction1 = hkpLinFrictionConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.friction2 = hkpLinFrictionConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.ang = hkpAngConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.linLimit0 = hkpLinLimitConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.linLimit1 = hkpLinLimitConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.linLimit2 = hkpLinLimitConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transforms={transforms}, motor={motor}, friction0={friction0}, friction1={friction1}, friction2={friction2}, ang={ang}, linLimit0={linLimit0}, linLimit1={linLimit1}, linLimit2={linLimit2}>".format(**{
            "class_name": self.__class__.__name__,
            "transforms": self.transforms,
            "motor": self.motor,
            "friction0": self.friction0,
            "friction1": self.friction1,
            "friction2": self.friction2,
            "ang": self.ang,
            "linLimit0": self.linLimit0,
            "linLimit1": self.linLimit1,
            "linLimit2": self.linLimit2,
        })
