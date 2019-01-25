from .hkReferencedObject import hkReferencedObject
from enum import Enum
import struct
from .hkpWorld import hkpWorld
from .enums import LastProcessingStep


class FindContacts(Enum):
    FIND_CONTACTS_DEFAULT = 0
    FIND_CONTACTS_EXTRA = 1


class ResetCollisionInformation(Enum):
    RESET_TOI = 1
    RESET_TIM = 2
    RESET_AABB = 4
    RESET_ALL = 7


class LastProcessingStep(Enum):
    INTEGRATE = 0
    COLLIDE = 1


class hkpSimulation(hkReferencedObject):
    determinismCheckFrameCounter: int
    world: any
    lastProcessingStep: LastProcessingStep
    currentTime: float
    currentPsiTime: float
    physicsDeltaTime: float
    simulateUntilTime: float
    frameMarkerPsiSnap: float
    previousStepResult: int

    def __init__(self, infile):
        self.determinismCheckFrameCounter = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.world = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.lastProcessingStep = LastProcessingStep(infile)  # TYPE_ENUM:TYPE_UINT8
        self.currentTime = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.currentPsiTime = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.physicsDeltaTime = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.simulateUntilTime = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.frameMarkerPsiSnap = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.previousStepResult = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} determinismCheckFrameCounter={determinismCheckFrameCounter}, world={world}, lastProcessingStep={lastProcessingStep}, currentTime={currentTime}, currentPsiTime={currentPsiTime}, physicsDeltaTime={physicsDeltaTime}, simulateUntilTime={simulateUntilTime}, frameMarkerPsiSnap={frameMarkerPsiSnap}, previousStepResult={previousStepResult}>".format(**{
            "class_name": self.__class__.__name__,
            "determinismCheckFrameCounter": self.determinismCheckFrameCounter,
            "world": self.world,
            "lastProcessingStep": self.lastProcessingStep,
            "currentTime": self.currentTime,
            "currentPsiTime": self.currentPsiTime,
            "physicsDeltaTime": self.physicsDeltaTime,
            "simulateUntilTime": self.simulateUntilTime,
            "frameMarkerPsiSnap": self.frameMarkerPsiSnap,
            "previousStepResult": self.previousStepResult,
        })
