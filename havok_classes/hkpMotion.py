from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .enums import MotionType
import struct
from .hkMotionState import hkMotionState
from .hkpMaxSizeMotion import hkpMaxSizeMotion


class MotionType(Enum):
    MOTION_INVALID = 0
    MOTION_DYNAMIC = 1
    MOTION_SPHERE_INERTIA = 2
    MOTION_BOX_INERTIA = 3
    MOTION_KEYFRAMED = 4
    MOTION_FIXED = 5
    MOTION_THIN_BOX_INERTIA = 6
    MOTION_CHARACTER = 7
    MOTION_MAX_ID = 8


class hkpMotion(hkReferencedObject):
    type: MotionType
    deactivationIntegrateCounter: int
    deactivationNumInactiveFrames: int
    motionState: hkMotionState
    inertiaAndMassInv: vector4
    linearVelocity: vector4
    angularVelocity: vector4
    deactivationRefPosition: vector4
    deactivationRefOrientation: int
    savedMotion: any
    savedQualityTypeIndex: int
    gravityFactor: int

    def __init__(self, infile):
        self.type = MotionType(infile)  # TYPE_ENUM:TYPE_UINT8
        self.deactivationIntegrateCounter = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.deactivationNumInactiveFrames = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.motionState = hkMotionState(infile)  # TYPE_STRUCT:TYPE_VOID
        self.inertiaAndMassInv = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.linearVelocity = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.angularVelocity = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.deactivationRefPosition = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.deactivationRefOrientation = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.savedMotion = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.savedQualityTypeIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.gravityFactor = struct.unpack('>h', infile.read(2))  # TYPE_HALF:TYPE_VOID

    def __repr__(self):
        return "<{class_name} type={type}, deactivationIntegrateCounter={deactivationIntegrateCounter}, deactivationNumInactiveFrames={deactivationNumInactiveFrames}, motionState={motionState}, inertiaAndMassInv={inertiaAndMassInv}, linearVelocity={linearVelocity}, angularVelocity={angularVelocity}, deactivationRefPosition={deactivationRefPosition}, deactivationRefOrientation={deactivationRefOrientation}, savedMotion={savedMotion}, savedQualityTypeIndex={savedQualityTypeIndex}, gravityFactor={gravityFactor}>".format(**{
            "class_name": self.__class__.__name__,
            "type": self.type,
            "deactivationIntegrateCounter": self.deactivationIntegrateCounter,
            "deactivationNumInactiveFrames": self.deactivationNumInactiveFrames,
            "motionState": self.motionState,
            "inertiaAndMassInv": self.inertiaAndMassInv,
            "linearVelocity": self.linearVelocity,
            "angularVelocity": self.angularVelocity,
            "deactivationRefPosition": self.deactivationRefPosition,
            "deactivationRefOrientation": self.deactivationRefOrientation,
            "savedMotion": self.savedMotion,
            "savedQualityTypeIndex": self.savedQualityTypeIndex,
            "gravityFactor": self.gravityFactor,
        })
