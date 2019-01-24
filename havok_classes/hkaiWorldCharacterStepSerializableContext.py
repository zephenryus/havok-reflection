from .hkReferencedObject import hkReferencedObject
from .common import any
from .enums import CharacterCallbackType
from .hkaiCharacter import hkaiCharacter
from .hkaiLocalSteeringInput import hkaiLocalSteeringInput
from .hkaiObstacleGenerator import hkaiObstacleGenerator


class hkaiWorldCharacterStepSerializableContext(hkReferencedObject):
    world: any
    callbackType: CharacterCallbackType
    timestep: float
    characters: hkaiCharacter
    localSteeringInputs: hkaiLocalSteeringInput
    obstacleGenerators: hkaiObstacleGenerator
