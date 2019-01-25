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
    world: hkpWorld
    lastProcessingStep: LastProcessingStep
    currentTime: float
    currentPsiTime: float
    physicsDeltaTime: float
    simulateUntilTime: float
    frameMarkerPsiSnap: float
    previousStepResult: int

    def __init__(self, infile):
        self.determinismCheckFrameCounter = struct.unpack('>I', infile.read(4))
        self.world = hkpWorld(infile)  # TYPE_POINTER
        self.lastProcessingStep = LastProcessingStep(infile)  # TYPE_ENUM
        self.currentTime = struct.unpack('>f', infile.read(4))
        self.currentPsiTime = struct.unpack('>f', infile.read(4))
        self.physicsDeltaTime = struct.unpack('>f', infile.read(4))
        self.simulateUntilTime = struct.unpack('>f', infile.read(4))
        self.frameMarkerPsiSnap = struct.unpack('>f', infile.read(4))
        self.previousStepResult = struct.unpack('>I', infile.read(4))
