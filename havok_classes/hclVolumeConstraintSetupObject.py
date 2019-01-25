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

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.simulationMesh = hclSimulationSetupMesh(infile)  # TYPE_POINTER
        self.applyToParticles = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.stiffness = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.influenceParticles = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.particleWeights = hclVertexFloatInput(infile)  # TYPE_STRUCT
