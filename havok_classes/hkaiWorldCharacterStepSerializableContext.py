from .hkReferencedObject import hkReferencedObject
from .common import any
from .enums import CharacterCallbackType
import struct
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

    def __init__(self, infile):
        self.world = any(infile)  # TYPE_POINTER
        self.callbackType = CharacterCallbackType(infile)  # TYPE_ENUM
        self.timestep = struct.unpack('>f', infile.read(4))
        self.characters = hkaiCharacter(infile)  # TYPE_ARRAY
        self.localSteeringInputs = hkaiLocalSteeringInput(infile)  # TYPE_ARRAY
        self.obstacleGenerators = hkaiObstacleGenerator(infile)  # TYPE_ARRAY
