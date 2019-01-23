from .hkReferencedObject import hkReferencedObject
from .hkpWorld import hkpWorld


class hkpSimulation(hkReferencedObject):
	determinismCheckFrameCounter: int
	world: hkpWorld
	lastProcessingStep: any
	currentTime: float
	currentPsiTime: float
	physicsDeltaTime: float
	simulateUntilTime: float
	frameMarkerPsiSnap: float
	previousStepResult: int
