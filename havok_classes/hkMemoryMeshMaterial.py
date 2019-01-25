from .hkMeshMaterial import hkMeshMaterial
from typing import List
from .common import get_array
from .hkMeshTexture import hkMeshTexture
import struct


class hkMemoryMeshMaterial(hkMeshMaterial):
    materialName: str
    textures: List[hkMeshTexture]
    diffuseColor: vector4
    ambientColor: vector4
    specularColor: vector4
    emissiveColor: vector4
    userData: int
    tesselationFactor: float
    displacementAmount: float

    def __init__(self, infile):
        self.materialName = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.textures = get_array(infile, hkMeshTexture, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.diffuseColor = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.ambientColor = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.specularColor = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.emissiveColor = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.userData = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID
        self.tesselationFactor = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.displacementAmount = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} materialName=\"{materialName}\", textures=[{textures}], diffuseColor={diffuseColor}, ambientColor={ambientColor}, specularColor={specularColor}, emissiveColor={emissiveColor}, userData={userData}, tesselationFactor={tesselationFactor}, displacementAmount={displacementAmount}>".format(**{
            "class_name": self.__class__.__name__,
            "materialName": self.materialName,
            "textures": self.textures,
            "diffuseColor": self.diffuseColor,
            "ambientColor": self.ambientColor,
            "specularColor": self.specularColor,
            "emissiveColor": self.emissiveColor,
            "userData": self.userData,
            "tesselationFactor": self.tesselationFactor,
            "displacementAmount": self.displacementAmount,
        })
