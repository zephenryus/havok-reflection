from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput


class hclVolumeConstraintSetupObject(hclConstraintSetSetupObject):
    name: str
    simulationMesh: any
    applyToParticles: hclVertexSelectionInput
    stiffness: hclVertexFloatInput
    influenceParticles: hclVertexSelectionInput
    particleWeights: hclVertexFloatInput

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.simulationMesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.applyToParticles = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.stiffness = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.influenceParticles = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.particleWeights = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", simulationMesh={simulationMesh}, applyToParticles={applyToParticles}, stiffness={stiffness}, influenceParticles={influenceParticles}, particleWeights={particleWeights}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "simulationMesh": self.simulationMesh,
            "applyToParticles": self.applyToParticles,
            "stiffness": self.stiffness,
            "influenceParticles": self.influenceParticles,
            "particleWeights": self.particleWeights,
        })
