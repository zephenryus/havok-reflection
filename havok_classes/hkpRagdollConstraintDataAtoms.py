from enum import Enum
from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpSetupStabilizationAtom import hkpSetupStabilizationAtom
from .hkpRagdollMotorConstraintAtom import hkpRagdollMotorConstraintAtom
from .hkpAngFrictionConstraintAtom import hkpAngFrictionConstraintAtom
from .hkpTwistLimitConstraintAtom import hkpTwistLimitConstraintAtom
from .hkpConeLimitConstraintAtom import hkpConeLimitConstraintAtom
from .hkpBallSocketConstraintAtom import hkpBallSocketConstraintAtom


class Axis(Enum):
    AXIS_TWIST = 0
    AXIS_PLANES = 1
    AXIS_CROSS_PRODUCT = 2


class hkpRagdollConstraintDataAtoms(object):
    transforms: hkpSetLocalTransformsConstraintAtom
    setupStabilization: hkpSetupStabilizationAtom
    ragdollMotors: hkpRagdollMotorConstraintAtom
    angFriction: hkpAngFrictionConstraintAtom
    twistLimit: hkpTwistLimitConstraintAtom
    coneLimit: hkpConeLimitConstraintAtom
    planesLimit: hkpConeLimitConstraintAtom
    ballSocket: hkpBallSocketConstraintAtom

    def __init__(self, infile):
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT
        self.setupStabilization = hkpSetupStabilizationAtom(infile)  # TYPE_STRUCT
        self.ragdollMotors = hkpRagdollMotorConstraintAtom(infile)  # TYPE_STRUCT
        self.angFriction = hkpAngFrictionConstraintAtom(infile)  # TYPE_STRUCT
        self.twistLimit = hkpTwistLimitConstraintAtom(infile)  # TYPE_STRUCT
        self.coneLimit = hkpConeLimitConstraintAtom(infile)  # TYPE_STRUCT
        self.planesLimit = hkpConeLimitConstraintAtom(infile)  # TYPE_STRUCT
        self.ballSocket = hkpBallSocketConstraintAtom(infile)  # TYPE_STRUCT
