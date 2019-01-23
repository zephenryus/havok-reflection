from .hkReferencedObject import hkReferencedObject
from .hkaiCharacter import hkaiCharacter
from .hkaiLocalSteeringInput import hkaiLocalSteeringInput
from .hkaiObstacleGenerator import hkaiObstacleGenerator


class hkaiWorldCharacterStepSerializableContext(hkReferencedObject):
	world: any
	callbackType: any
	timestep: float
	characters: hkaiCharacter
	localSteeringInputs: hkaiLocalSteeringInput
	obstacleGenerators: hkaiObstacleGenerator
