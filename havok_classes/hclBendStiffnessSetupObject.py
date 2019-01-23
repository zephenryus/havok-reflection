from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput


class hclBendStiffnessSetupObject(hclConstraintSetSetupObject):
	name: any
	simulationMesh: hclSimulationSetupMesh
	vertexSelection: hclVertexSelectionInput
	bendStiffness: hclVertexFloatInput
	useRestPoseConfig: bool
