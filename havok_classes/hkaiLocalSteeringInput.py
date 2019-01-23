

class hkaiLocalSteeringInput(object):
	currentPosition: any
	currentForward: any
	currentUp: any
	currentVelocity: any
	desiredVelocity: any
	localGoalPlane: any
	distToLocalGoal: float
	character: any
	referenceFrame: any
	avoidanceProperties: any
	applyKinematicConstraints: bool
	applyAvoidanceSteering: bool
	enableLocalSteering: bool
