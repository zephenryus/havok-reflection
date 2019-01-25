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
    simClothSetupObject: any

    def __init__(self, infile):
        self.type = Type(infile)  # TYPE_ENUM:TYPE_UINT32
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.simClothSetupObject = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} type={type}, name=\"{name}\", simClothSetupObject={simClothSetupObject}>".format(**{
            "class_name": self.__class__.__name__,
            "type": self.type,
            "name": self.name,
            "simClothSetupObject": self.simClothSetupObject,
        })
