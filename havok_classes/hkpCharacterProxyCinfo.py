from .hkpCharacterControllerCinfo import hkpCharacterControllerCinfo
import struct
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
    shapePhantom: any
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

    def __init__(self, infile):
        self.position = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.velocity = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.dynamicFriction = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.staticFriction = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.keepContactTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.up = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.extraUpStaticFriction = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.extraDownStaticFriction = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.shapePhantom = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.keepDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.contactAngleSensitivity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.userPlanes = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.maxCharacterSpeedForSolver = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.characterStrength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.characterMass = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxSlope = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.penetrationRecoverySpeed = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxCastIterations = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.refreshManifoldInCheckSupport = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} position={position}, velocity={velocity}, dynamicFriction={dynamicFriction}, staticFriction={staticFriction}, keepContactTolerance={keepContactTolerance}, up={up}, extraUpStaticFriction={extraUpStaticFriction}, extraDownStaticFriction={extraDownStaticFriction}, shapePhantom={shapePhantom}, keepDistance={keepDistance}, contactAngleSensitivity={contactAngleSensitivity}, userPlanes={userPlanes}, maxCharacterSpeedForSolver={maxCharacterSpeedForSolver}, characterStrength={characterStrength}, characterMass={characterMass}, maxSlope={maxSlope}, penetrationRecoverySpeed={penetrationRecoverySpeed}, maxCastIterations={maxCastIterations}, refreshManifoldInCheckSupport={refreshManifoldInCheckSupport}>".format(**{
            "class_name": self.__class__.__name__,
            "position": self.position,
            "velocity": self.velocity,
            "dynamicFriction": self.dynamicFriction,
            "staticFriction": self.staticFriction,
            "keepContactTolerance": self.keepContactTolerance,
            "up": self.up,
            "extraUpStaticFriction": self.extraUpStaticFriction,
            "extraDownStaticFriction": self.extraDownStaticFriction,
            "shapePhantom": self.shapePhantom,
            "keepDistance": self.keepDistance,
            "contactAngleSensitivity": self.contactAngleSensitivity,
            "userPlanes": self.userPlanes,
            "maxCharacterSpeedForSolver": self.maxCharacterSpeedForSolver,
            "characterStrength": self.characterStrength,
            "characterMass": self.characterMass,
            "maxSlope": self.maxSlope,
            "penetrationRecoverySpeed": self.penetrationRecoverySpeed,
            "maxCastIterations": self.maxCastIterations,
            "refreshManifoldInCheckSupport": self.refreshManifoldInCheckSupport,
        })
