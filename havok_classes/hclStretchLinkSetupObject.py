from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
from .common import vector4


class hclStretchLinkSetupObject(hclConstraintSetSetupObject):
    name: str
    simulationMesh: hclSimulationSetupMesh
    movableParticlesSelection: hclVertexSelectionInput
    fixedParticlesSelection: hclVertexSelectionInput
    rigidFactor: hclVertexFloatInput
    stiffness: hclVertexFloatInput
    stretchDirection: vector4
    useStretchDirection: bool
    useMeshTopology: bool
    allowDynamicLinks: bool
    useTopologicalStretchDistance: bool
