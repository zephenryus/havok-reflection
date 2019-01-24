from .hkReferencedObject import hkReferencedObject
from enum import Enum
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
