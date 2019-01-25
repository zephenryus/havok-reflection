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
        self.linearIsFixed = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.transforms = hkpSetLocalTransformsConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.setupStabilization = hkpSetupStabilizationAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.ragdollMotors = hkpRagdollMotorConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.angFriction = hkpAngFrictionConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.twistLimit = hkpTwistLimitConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.ellipticalLimit = hkpEllipticalLimitConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.stiffSpring = hkpStiffSpringConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.linearMotor0 = hkpLinMotorConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.linearMotor1 = hkpLinMotorConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.linearMotor2 = hkpLinMotorConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.ballSocket = hkpBallSocketConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} linearIsFixed={linearIsFixed}, transforms={transforms}, setupStabilization={setupStabilization}, ragdollMotors={ragdollMotors}, angFriction={angFriction}, twistLimit={twistLimit}, ellipticalLimit={ellipticalLimit}, stiffSpring={stiffSpring}, linearMotor0={linearMotor0}, linearMotor1={linearMotor1}, linearMotor2={linearMotor2}, ballSocket={ballSocket}>".format(**{
            "class_name": self.__class__.__name__,
            "linearIsFixed": self.linearIsFixed,
            "transforms": self.transforms,
            "setupStabilization": self.setupStabilization,
            "ragdollMotors": self.ragdollMotors,
            "angFriction": self.angFriction,
            "twistLimit": self.twistLimit,
            "ellipticalLimit": self.ellipticalLimit,
            "stiffSpring": self.stiffSpring,
            "linearMotor0": self.linearMotor0,
            "linearMotor1": self.linearMotor1,
            "linearMotor2": self.linearMotor2,
            "ballSocket": self.ballSocket,
        })
