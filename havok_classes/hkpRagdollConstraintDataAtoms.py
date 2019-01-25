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
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.setupStabilization = hkpSetupStabilizationAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.ragdollMotors = hkpRagdollMotorConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.angFriction = hkpAngFrictionConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.twistLimit = hkpTwistLimitConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.coneLimit = hkpConeLimitConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.planesLimit = hkpConeLimitConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.ballSocket = hkpBallSocketConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transforms={transforms}, setupStabilization={setupStabilization}, ragdollMotors={ragdollMotors}, angFriction={angFriction}, twistLimit={twistLimit}, coneLimit={coneLimit}, planesLimit={planesLimit}, ballSocket={ballSocket}>".format(**{
            "class_name": self.__class__.__name__,
            "transforms": self.transforms,
            "setupStabilization": self.setupStabilization,
            "ragdollMotors": self.ragdollMotors,
            "angFriction": self.angFriction,
            "twistLimit": self.twistLimit,
            "coneLimit": self.coneLimit,
            "planesLimit": self.planesLimit,
            "ballSocket": self.ballSocket,
        })
