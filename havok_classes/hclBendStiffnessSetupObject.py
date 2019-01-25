from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
import struct


class hclBendStiffnessSetupObject(hclConstraintSetSetupObject):
    name: str
    simulationMesh: hclSimulationSetupMesh
    vertexSelection: hclVertexSelectionInput
    bendStiffness: hclVertexFloatInput
    useRestPoseConfig: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.simulationMesh = hclSimulationSetupMesh(infile)  # TYPE_POINTER
        self.vertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.bendStiffness = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.useRestPoseConfig = struct.unpack('>?', infile.read(1))
