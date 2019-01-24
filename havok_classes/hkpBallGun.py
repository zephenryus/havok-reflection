from .hkpFirstPersonGun import hkpFirstPersonGun
from .common import vector4, any


class hkpBallGun(hkpFirstPersonGun):
    bulletRadius: float
    bulletVelocity: float
    bulletMass: float
    damageMultiplier: float
    maxBulletsInWorld: int
    bulletOffsetFromCenter: vector4
    addedBodies: any
