from .hkMeshMaterial import hkMeshMaterial
from .hkMeshTexture import hkMeshTexture


class hkMemoryMeshMaterial(hkMeshMaterial):
	materialName: any
	textures: hkMeshTexture
	diffuseColor: any
	ambientColor: any
	specularColor: any
	emissiveColor: any
	userData: int
	tesselationFactor: float
	displacementAmount: float
