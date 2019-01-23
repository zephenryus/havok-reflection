from .hkpFirstPersonGun import hkpFirstPersonGun


class hkpBallGun(hkpFirstPersonGun):
	bulletRadius: float
	bulletVelocity: float
	bulletMass: float
	damageMultiplier: float
	maxBulletsInWorld: int
	bulletOffsetFromCenter: any
	addedBodies: any
