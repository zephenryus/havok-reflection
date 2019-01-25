from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
import struct
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput


class hclBendLinkSetupObject(hclConstraintSetSetupObject):
    name: str
    simulationMesh: hclSimulationSetupMesh
    createStandardLinks: bool
    vertexSelection: hclVertexSelectionInput
    bendStiffness: hclVertexFloatInput
    stretchStiffness: hclVertexFloatInput
    flatnessFactor: hclVertexFloatInput

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.simulationMesh = hclSimulationSetupMesh(infile)  # TYPE_POINTER
        self.createStandardLinks = struct.unpack('>?', infile.read(1))
        self.vertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.bendStiffness = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.stretchStiffness = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.flatnessFactor = hclVertexFloatInput(infile)  # TYPE_STRUCT
