from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput


class hclVolumeConstraintSetupObject(hclConstraintSetSetupObject):
    name: str
    simulationMesh: hclSimulationSetupMesh
    applyToParticles: hclVertexSelectionInput
    stiffness: hclVertexFloatInput
    influenceParticles: hclVertexSelectionInput
    particleWeights: hclVertexFloatInput
