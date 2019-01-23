from .hkReferencedObject import hkReferencedObject
from .hkMotionState import hkMotionState
from .hkpMaxSizeMotion import hkpMaxSizeMotion


class hkpMotion(hkReferencedObject):
	type: any
	deactivationIntegrateCounter: int
	deactivationNumInactiveFrames: int
	motionState: hkMotionState
	inertiaAndMassInv: any
	linearVelocity: any
	angularVelocity: any
	deactivationRefPosition: any
	deactivationRefOrientation: int
	savedMotion: hkpMaxSizeMotion
	savedQualityTypeIndex: int
	gravityFactor: int
