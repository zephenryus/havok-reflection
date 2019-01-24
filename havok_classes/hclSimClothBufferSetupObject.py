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
