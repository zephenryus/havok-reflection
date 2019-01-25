from .hkpCharacterControllerCinfo import hkpCharacterControllerCinfo
import struct
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

    def __init__(self, infile):
        self.collisionFilterInfo = struct.unpack('>I', infile.read(4))
        self.shape = hkpShape(infile)  # TYPE_POINTER
        self.position = struct.unpack('>4f', infile.read(16))
        self.rotation = any(infile)  # TYPE_QUATERNION
        self.mass = struct.unpack('>f', infile.read(4))
        self.friction = struct.unpack('>f', infile.read(4))
        self.maxLinearVelocity = struct.unpack('>f', infile.read(4))
        self.allowedPenetrationDepth = struct.unpack('>f', infile.read(4))
        self.up = struct.unpack('>4f', infile.read(16))
        self.maxSlope = struct.unpack('>f', infile.read(4))
        self.maxForce = struct.unpack('>f', infile.read(4))
        self.unweldingHeightOffsetFactor = struct.unpack('>f', infile.read(4))
        self.maxSpeedForSimplexSolver = struct.unpack('>f', infile.read(4))
        self.supportDistance = struct.unpack('>f', infile.read(4))
        self.hardSupportDistance = struct.unpack('>f', infile.read(4))
        self.vdbColor = struct.unpack('>i', infile.read(4))
