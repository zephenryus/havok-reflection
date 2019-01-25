from .hkpCharacterControllerCinfo import hkpCharacterControllerCinfo
import struct
from .hkpShape import hkpShape


class hkpCharacterRigidBodyCinfo(hkpCharacterControllerCinfo):
    collisionFilterInfo: int
    shape: any
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
        self.collisionFilterInfo = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.shape = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.position = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.rotation = any(infile)  # TYPE_QUATERNION:TYPE_VOID
        self.mass = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.friction = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxLinearVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.allowedPenetrationDepth = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.up = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.maxSlope = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxForce = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.unweldingHeightOffsetFactor = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxSpeedForSimplexSolver = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.supportDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.hardSupportDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.vdbColor = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} collisionFilterInfo={collisionFilterInfo}, shape={shape}, position={position}, rotation={rotation}, mass={mass}, friction={friction}, maxLinearVelocity={maxLinearVelocity}, allowedPenetrationDepth={allowedPenetrationDepth}, up={up}, maxSlope={maxSlope}, maxForce={maxForce}, unweldingHeightOffsetFactor={unweldingHeightOffsetFactor}, maxSpeedForSimplexSolver={maxSpeedForSimplexSolver}, supportDistance={supportDistance}, hardSupportDistance={hardSupportDistance}, vdbColor={vdbColor}>".format(**{
            "class_name": self.__class__.__name__,
            "collisionFilterInfo": self.collisionFilterInfo,
            "shape": self.shape,
            "position": self.position,
            "rotation": self.rotation,
            "mass": self.mass,
            "friction": self.friction,
            "maxLinearVelocity": self.maxLinearVelocity,
            "allowedPenetrationDepth": self.allowedPenetrationDepth,
            "up": self.up,
            "maxSlope": self.maxSlope,
            "maxForce": self.maxForce,
            "unweldingHeightOffsetFactor": self.unweldingHeightOffsetFactor,
            "maxSpeedForSimplexSolver": self.maxSpeedForSimplexSolver,
            "supportDistance": self.supportDistance,
            "hardSupportDistance": self.hardSupportDistance,
            "vdbColor": self.vdbColor,
        })
