from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .enums import ShaderType
from typing import List
from .common import get_array


class ShaderType(Enum):
    EFFECT_TYPE_INVALID = 0
    EFFECT_TYPE_UNKNOWN = 1
    EFFECT_TYPE_HLSL_INLINE = 2
    EFFECT_TYPE_CG_INLINE = 3
    EFFECT_TYPE_HLSL_FILENAME = 4
    EFFECT_TYPE_CG_FILENAME = 5
    EFFECT_TYPE_MAX_ID = 6


class hkxMaterialShader(hkReferencedObject):
    name: str
    type: ShaderType
    vertexEntryName: str
    geomEntryName: str
    pixelEntryName: str
    data: List[int]

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.type = ShaderType(infile)  # TYPE_ENUM:TYPE_UINT8
        self.vertexEntryName = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.geomEntryName = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.pixelEntryName = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.data = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} name=\"{name}\", type={type}, vertexEntryName=\"{vertexEntryName}\", geomEntryName=\"{geomEntryName}\", pixelEntryName=\"{pixelEntryName}\", data=[{data}]>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "type": self.type,
            "vertexEntryName": self.vertexEntryName,
            "geomEntryName": self.geomEntryName,
            "pixelEntryName": self.pixelEntryName,
            "data": self.data,
        })
