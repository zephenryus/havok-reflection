from .hkpFirstPersonGun import hkpFirstPersonGun


class hkpGravityGun(hkpFirstPersonGun):
	grabbedBodies: any
	maxNumObjectsPicked: int
	maxMassOfObjectPicked: float
	maxDistOfObjectPicked: float
	impulseAppliedWhenObjectNotPicked: float
	throwVelocity: float
	capturedObjectPosition: any
	capturedObjectsOffset: any
