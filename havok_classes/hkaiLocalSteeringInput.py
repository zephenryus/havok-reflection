from .common import vector4, any


class hkaiLocalSteeringInput(object):
    currentPosition: vector4
    currentForward: vector4
    currentUp: vector4
    currentVelocity: vector4
    desiredVelocity: vector4
    localGoalPlane: vector4
    distToLocalGoal: float
    character: any
    referenceFrame: any
    avoidanceProperties: any
    applyKinematicConstraints: bool
    applyAvoidanceSteering: bool
    enableLocalSteering: bool
