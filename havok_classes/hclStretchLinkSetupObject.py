from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
from .hclVertexFloatInput import hclVertexFloatInput


class hclStretchLinkSetupObject(hclConstraintSetSetupObject):
	name: any
	simulationMesh: hclSimulationSetupMesh
	movableParticlesSelection: hclVertexSelectionInput
	fixedParticlesSelection: hclVertexSelectionInput
	rigidFactor: hclVertexFloatInput
	stiffness: hclVertexFloatInput
	stretchDirection: any
	useStretchDirection: bool
	useMeshTopology: bool
	allowDynamicLinks: bool
	useTopologicalStretchDistance: bool
