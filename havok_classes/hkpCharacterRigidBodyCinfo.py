from .hkpCharacterControllerCinfo import hkpCharacterControllerCinfo
from .hkpShape import hkpShape


class hkpCharacterRigidBodyCinfo(hkpCharacterControllerCinfo):
	collisionFilterInfo: int
	shape: hkpShape
	position: any
	rotation: any
	mass: float
	friction: float
	maxLinearVelocity: float
	allowedPenetrationDepth: float
	up: any
	maxSlope: float
	maxForce: float
	unweldingHeightOffsetFactor: float
	maxSpeedForSimplexSolver: float
	supportDistance: float
	hardSupportDistance: float
	vdbColor: int
