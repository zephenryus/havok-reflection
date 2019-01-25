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
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.motor = hkpLinMotorConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.friction = hkpLinFrictionConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.ang = hkpAngConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.lin0 = hkpLinConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.lin1 = hkpLinConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.linLimit = hkpLinLimitConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transforms={transforms}, motor={motor}, friction={friction}, ang={ang}, lin0={lin0}, lin1={lin1}, linLimit={linLimit}>".format(**{
            "class_name": self.__class__.__name__,
            "transforms": self.transforms,
            "motor": self.motor,
            "friction": self.friction,
            "ang": self.ang,
            "lin0": self.lin0,
            "lin1": self.lin1,
            "linLimit": self.linLimit,
        })
