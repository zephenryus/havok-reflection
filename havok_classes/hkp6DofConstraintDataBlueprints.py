import struct
from .hkpSetLocalTransformsConstraintAtom import hkpSetLocalTransformsConstraintAtom
from .hkpSetupStabilizationAtom import hkpSetupStabilizationAtom
from .hkpRagdollMotorConstraintAtom import hkpRagdollMotorConstraintAtom
from .hkpAngFrictionConstraintAtom import hkpAngFrictionConstraintAtom
from .hkpTwistLimitConstraintAtom import hkpTwistLimitConstraintAtom
from .hkpEllipticalLimitConstraintAtom import hkpEllipticalLimitConstraintAtom
from .hkpStiffSpringConstraintAtom import hkpStiffSpringConstraintAtom
from .hkpLinMotorConstraintAtom import hkpLinMotorConstraintAtom
from .hkpBallSocketConstraintAtom import hkpBallSocketConstraintAtom


class hkp6DofConstraintDataBlueprints(object):
    linearIsFixed: bool
    transforms: hkpSetLocalTransformsConstraintAtom
    setupStabilization: hkpSetupStabilizationAtom
    ragdollMotors: hkpRagdollMotorConstraintAtom
    angFriction: hkpAngFrictionConstraintAtom
    twistLimit: hkpTwistLimitConstraintAtom
    ellipticalLimit: hkpEllipticalLimitConstraintAtom
    stiffSpring: hkpStiffSpringConstraintAtom
    linearMotor0: hkpLinMotorConstraintAtom
    linearMotor1: hkpLinMotorConstraintAtom
    linearMotor2: hkpLinMotorConstraintAtom
    ballSocket: hkpBallSocketConstraintAtom

    def __init__(self, infile):
        self.linearIsFixed = struct.unpack('>?', infile.read(1))
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT
        self.setupStabilization = hkpSetupStabilizationAtom(infile)  # TYPE_STRUCT
        self.ragdollMotors = hkpRagdollMotorConstraintAtom(infile)  # TYPE_STRUCT
        self.angFriction = hkpAngFrictionConstraintAtom(infile)  # TYPE_STRUCT
        self.twistLimit = hkpTwistLimitConstraintAtom(infile)  # TYPE_STRUCT
        self.ellipticalLimit = hkpEllipticalLimitConstraintAtom(infile)  # TYPE_STRUCT
        self.stiffSpring = hkpStiffSpringConstraintAtom(infile)  # TYPE_STRUCT
        self.linearMotor0 = hkpLinMotorConstraintAtom(infile)  # TYPE_STRUCT
        self.linearMotor1 = hkpLinMotorConstraintAtom(infile)  # TYPE_STRUCT
        self.linearMotor2 = hkpLinMotorConstraintAtom(infile)  # TYPE_STRUCT
        self.ballSocket = hkpBallSocketConstraintAtom(infile)  # TYPE_STRUCT
