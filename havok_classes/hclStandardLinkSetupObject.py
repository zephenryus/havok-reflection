from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclEdgeSelectionInput import hclEdgeSelectionInput
import struct
from .hclVertexFloatInput import hclVertexFloatInput


class hclStandardLinkSetupObject(hclConstraintSetSetupObject):
    name: str
    simulationMesh: hclSimulationSetupMesh
    vertexSelection: hclVertexSelectionInput
    edgeSelection: hclEdgeSelectionInput
    ignoreHiddenEdges: bool
    stiffness: hclVertexFloatInput
    allowedCompression: hclVertexFloatInput
    allowedStretching: hclVertexFloatInput

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.simulationMesh = hclSimulationSetupMesh(infile)  # TYPE_POINTER
        self.vertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.edgeSelection = hclEdgeSelectionInput(infile)  # TYPE_STRUCT
        self.ignoreHiddenEdges = struct.unpack('>?', infile.read(1))
        self.stiffness = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.allowedCompression = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.allowedStretching = hclVertexFloatInput(infile)  # TYPE_STRUCT
