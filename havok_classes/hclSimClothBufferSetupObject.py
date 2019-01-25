from .hclBufferSetupObject import hclBufferSetupObject
from enum import Enum
from .enums import Type
from .hclSimClothSetupObject import hclSimClothSetupObject


class Type(Enum):
    SIM_CLOTH_MESH_CURRENT_POSITIONS = 0
    SIM_CLOTH_MESH_PREVIOUS_POSITIONS = 1
    SIM_CLOTH_MESH_ORIGINAL_POSE = 2


class hclSimClothBufferSetupObject(hclBufferSetupObject):
    type: Type
    name: str
    simClothSetupObject: hclSimClothSetupObject

    def __init__(self, infile):
        self.type = Type(infile)  # TYPE_ENUM
        self.name = struct.unpack('>s', infile.read(0))
        self.simClothSetupObject = hclSimClothSetupObject(infile)  # TYPE_POINTER
