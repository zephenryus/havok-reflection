from .hkUFloat8 import hkUFloat8
from .hkUFloat8 import hkUFloat8


class hkMotionState(object):
	transform: any
	sweptTransform: any
	deltaAngle: any
	objectRadius: float
	linearDamping: int
	angularDamping: int
	timeFactor: int
	maxLinearVelocity: hkUFloat8
	maxAngularVelocity: hkUFloat8
	deactivationClass: int
