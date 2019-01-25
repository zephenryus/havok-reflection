from .hkReferencedObject import hkReferencedObject
from .enums import CharacterCallbackType
import struct
from typing import List
from .common import get_array
from .hkaiCharacter import hkaiCharacter
from .hkaiLocalSteeringInput import hkaiLocalSteeringInput
from .hkaiObstacleGenerator import hkaiObstacleGenerator


class hkaiWorldCharacterStepSerializableContext(hkReferencedObject):
    world: any
    callbackType: CharacterCallbackType
    timestep: float
    characters: List[hkaiCharacter]
    localSteeringInputs: List[hkaiLocalSteeringInput]
    obstacleGenerators: List[hkaiObstacleGenerator]

    def __init__(self, infile):
        self.world = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.callbackType = CharacterCallbackType(infile)  # TYPE_ENUM:TYPE_UINT8
        self.timestep = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.characters = get_array(infile, hkaiCharacter, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.localSteeringInputs = get_array(infile, hkaiLocalSteeringInput, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.obstacleGenerators = get_array(infile, hkaiObstacleGenerator, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} world={world}, callbackType={callbackType}, timestep={timestep}, characters=[{characters}], localSteeringInputs=[{localSteeringInputs}], obstacleGenerators=[{obstacleGenerators}]>".format(**{
            "class_name": self.__class__.__name__,
            "world": self.world,
            "callbackType": self.callbackType,
            "timestep": self.timestep,
            "characters": self.characters,
            "localSteeringInputs": self.localSteeringInputs,
            "obstacleGenerators": self.obstacleGenerators,
        })
