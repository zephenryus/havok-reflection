from .hkpCharacterControllerCinfo import hkpCharacterControllerCinfo
from .hkpShape import hkpShape
from .common import vector4, any


class hkpCharacterRigidBodyCinfo(hkpCharacterControllerCinfo):
    collisionFilterInfo: int
    shape: hkpShape
    position: vector4
    rotation: any
    mass: float
    friction: float
    maxLinearVelocity: float
    allowedPenetrationDepth: float
    up: vector4
    maxSlope: float
    maxForce: float
    unweldingHeightOffsetFactor: float
    maxSpeedForSimplexSolver: float
    supportDistance: float
    hardSupportDistance: float
    vdbColor: int
