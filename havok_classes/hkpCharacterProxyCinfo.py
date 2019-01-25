from .hkpCharacterControllerCinfo import hkpCharacterControllerCinfo
from .common import vector4
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

    def __init__(self, infile):
        self.position = struct.unpack('>4f', infile.read(16))
        self.velocity = struct.unpack('>4f', infile.read(16))
        self.dynamicFriction = struct.unpack('>f', infile.read(4))
        self.staticFriction = struct.unpack('>f', infile.read(4))
        self.keepContactTolerance = struct.unpack('>f', infile.read(4))
        self.up = struct.unpack('>4f', infile.read(16))
        self.extraUpStaticFriction = struct.unpack('>f', infile.read(4))
        self.extraDownStaticFriction = struct.unpack('>f', infile.read(4))
        self.shapePhantom = hkpShapePhantom(infile)  # TYPE_POINTER
        self.keepDistance = struct.unpack('>f', infile.read(4))
        self.contactAngleSensitivity = struct.unpack('>f', infile.read(4))
        self.userPlanes = struct.unpack('>I', infile.read(4))
        self.maxCharacterSpeedForSolver = struct.unpack('>f', infile.read(4))
        self.characterStrength = struct.unpack('>f', infile.read(4))
        self.characterMass = struct.unpack('>f', infile.read(4))
        self.maxSlope = struct.unpack('>f', infile.read(4))
        self.penetrationRecoverySpeed = struct.unpack('>f', infile.read(4))
        self.maxCastIterations = struct.unpack('>i', infile.read(4))
        self.refreshManifoldInCheckSupport = struct.unpack('>?', infile.read(1))
