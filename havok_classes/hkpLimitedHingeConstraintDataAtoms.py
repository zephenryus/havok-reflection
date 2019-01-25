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
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT
        self.setupStabilization = hkpSetupStabilizationAtom(infile)  # TYPE_STRUCT
        self.angMotor = hkpAngMotorConstraintAtom(infile)  # TYPE_STRUCT
        self.angFriction = hkpAngFrictionConstraintAtom(infile)  # TYPE_STRUCT
        self.angLimit = hkpAngLimitConstraintAtom(infile)  # TYPE_STRUCT
        self.2dAng = hkp2dAngConstraintAtom(infile)  # TYPE_STRUCT
        self.ballSocket = hkpBallSocketConstraintAtom(infile)  # TYPE_STRUCT
