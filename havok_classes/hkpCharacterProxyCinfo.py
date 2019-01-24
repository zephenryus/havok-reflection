from .hkpCharacterControllerCinfo import hkpCharacterControllerCinfo
from .common import vector4
from .hkpShapePhantom import hkpShapePhantom


class hkpCharacterProxyCinfo(hkpCharacterControllerCinfo):
    position: vector4
    velocity: vector4
    dynamicFriction: float
    staticFriction: float
    keepContactTolerance: float
    up: vector4
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
