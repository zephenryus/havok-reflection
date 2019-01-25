from enum import Enum
from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpSetupStabilizationAtom import hkpSetupStabilizationAtom
from .hkpAngMotorConstraintAtom import hkpAngMotorConstraintAtom
from .hkpAngFrictionConstraintAtom import hkpAngFrictionConstraintAtom
from .hkpAngLimitConstraintAtom import hkpAngLimitConstraintAtom
from .hkp2dAngConstraintAtom import hkp2dAngConstraintAtom
from .hkpBallSocketConstraintAtom import hkpBallSocketConstraintAtom


class Axis(Enum):
    AXIS_AXLE = 0
    AXIS_PERP_TO_AXLE_1 = 1
    AXIS_PERP_TO_AXLE_2 = 2


class hkpLimitedHingeConstraintDataAtoms(object):
    transforms: hkpSetLocalTransformsConstraintAtom
    setupStabilization: hkpSetupStabilizationAtom
    angMotor: hkpAngMotorConstraintAtom
    angFriction: hkpAngFrictionConstraintAtom
    angLimit: hkpAngLimitConstraintAtom
    2dAng: hkp2dAngConstraintAtom
    ballSocket: hkpBallSocketConstraintAtom

    def __init__(self, infile):
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.setupStabilization = hkpSetupStabilizationAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.angMotor = hkpAngMotorConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.angFriction = hkpAngFrictionConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.angLimit = hkpAngLimitConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.2dAng = hkp2dAngConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.ballSocket = hkpBallSocketConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transforms={transforms}, setupStabilization={setupStabilization}, angMotor={angMotor}, angFriction={angFriction}, angLimit={angLimit}, 2dAng={2dAng}, ballSocket={ballSocket}>".format(**{
            "class_name": self.__class__.__name__,
            "transforms": self.transforms,
            "setupStabilization": self.setupStabilization,
            "angMotor": self.angMotor,
            "angFriction": self.angFriction,
            "angLimit": self.angLimit,
            "2dAng": self.2dAng,
            "ballSocket": self.ballSocket,
        })
