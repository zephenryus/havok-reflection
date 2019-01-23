from .hkReferencedObject import hkReferencedObject
from .hclSceneDataSetupMesh import hclSceneDataSetupMesh
from .hkxMeshSection import hkxMeshSection


class hclSceneDataSetupMeshSection(hkReferencedObject):
	setupMesh: hclSceneDataSetupMesh
	meshSection: hkxMeshSection
	skinnedSection: bool
