from .hkMeshMaterial import hkMeshMaterial
from .hkMeshTexture import hkMeshTexture
from .common import vector4


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
