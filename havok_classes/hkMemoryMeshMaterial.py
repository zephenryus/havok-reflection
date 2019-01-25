from .hkMeshMaterial import hkMeshMaterial
from .hkMeshTexture import hkMeshTexture
from .common import vector4
import struct


class hkMemoryMeshMaterial(hkMeshMaterial):
    materialName: str
    textures: hkMeshTexture
    diffuseColor: vector4
    ambientColor: vector4
    specularColor: vector4
    emissiveColor: vector4
    userData: int
    tesselationFactor: float
    displacementAmount: float

    def __init__(self, infile):
        self.materialName = struct.unpack('>s', infile.read(0))
        self.textures = hkMeshTexture(infile)  # TYPE_ARRAY
        self.diffuseColor = struct.unpack('>4f', infile.read(16))
        self.ambientColor = struct.unpack('>4f', infile.read(16))
        self.specularColor = struct.unpack('>4f', infile.read(16))
        self.emissiveColor = struct.unpack('>4f', infile.read(16))
        self.userData = struct.unpack('>L', infile.read(8))
        self.tesselationFactor = struct.unpack('>f', infile.read(4))
        self.displacementAmount = struct.unpack('>f', infile.read(4))
