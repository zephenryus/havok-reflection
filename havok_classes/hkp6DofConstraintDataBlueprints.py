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
