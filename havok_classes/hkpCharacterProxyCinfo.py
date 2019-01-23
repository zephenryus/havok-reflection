from .hkpCharacterControllerCinfo import hkpCharacterControllerCinfo
from .hkpShapePhantom import hkpShapePhantom


class hkpCharacterProxyCinfo(hkpCharacterControllerCinfo):
	position: any
	velocity: any
	dynamicFriction: float
	staticFriction: float
	keepContactTolerance: float
	up: any
	extraUpStaticFriction: float
	extraDownStaticFriction: float
	shapePhantom: hkpShapePhantom
	keepDistance: float
	contactAngleSensitivity: float
	userPlanes: int
	maxCharacterSpeedForSolver: float
	characterStrength: float
	characterMass: float
	maxSlope: float
	penetrationRecoverySpeed: float
	maxCastIterations: int
	refreshManifoldInCheckSupport: bool
