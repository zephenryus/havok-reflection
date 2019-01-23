from .hkxAttributeHolder import hkxAttributeHolder
from .hkxMaterialTextureStage import hkxMaterialTextureStage
from .hkxMaterial import hkxMaterial
from .hkReferencedObject import hkReferencedObject
from .hkxMaterialProperty import hkxMaterialProperty


class hkxMaterial(hkxAttributeHolder):
	name: any
	stages: hkxMaterialTextureStage
	diffuseColor: any
	ambientColor: any
	specularColor: any
	emissiveColor: any
	subMaterials: hkxMaterial
	extraData: hkReferencedObject
	uvMapScale: float
	uvMapOffset: float
	uvMapRotation: float
	uvMapAlgorithm: any
	specularMultiplier: float
	specularExponent: float
	transparency: any
	userData: int
	properties: hkxMaterialProperty
