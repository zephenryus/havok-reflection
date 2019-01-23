from .hclSetupMesh import hclSetupMesh
from .hclSetupMesh import hclSetupMesh
from .hclSimulationSetupMeshMapOptions import hclSimulationSetupMeshMapOptions


class hclSimulationSetupMesh(hclSetupMesh):
	originalMesh: hclSetupMesh
	mergeOptions: hclSimulationSetupMeshMapOptions
	mergedMeshMap: any
	worldFromOriginalMesh: any
	worldFromOriginalMeshInvTranspose: any
	originalMeshSections: any
	haveWorldTransforms: bool
