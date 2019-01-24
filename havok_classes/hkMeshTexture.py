from .hkReferencedObject import hkReferencedObject
from enum import Enum


class Format(Enum):
    Unknown = 0
    PNG = 1
    TGA = 2
    BMP = 3
    DDS = 4
    RAW = 5


class FilterMode(Enum):
    POINT = 0
    LINEAR = 1
    ANISOTROPIC = 2


class TextureUsageType(Enum):
    UNKNOWN = 0
    DIFFUSE = 1
    REFLECTION = 2
    BUMP = 3
    NORMAL = 4
    DISPLACEMENT = 5
    SPECULAR = 6
    SPECULARANDGLOSS = 7
    OPACITY = 8
    EMISSIVE = 9
    REFRACTION = 10
    GLOSS = 11
    DOMINANTS = 12
    NOTEXPORTED = 13


class hkMeshTexture(hkReferencedObject):
    pass
