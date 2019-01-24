from .hkpFirstPersonGun import hkpFirstPersonGun
from .common import any, vector4


class hkpGravityGun(hkpFirstPersonGun):
    grabbedBodies: any
    maxNumObjectsPicked: int
    maxMassOfObjectPicked: float
    maxDistOfObjectPicked: float
    impulseAppliedWhenObjectNotPicked: float
    throwVelocity: float
    capturedObjectPosition: vector4
    capturedObjectsOffset: vector4
