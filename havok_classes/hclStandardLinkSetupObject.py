from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclEdgeSelectionInput import hclEdgeSelectionInput
import struct
from .hclVertexFloatInput import hclVertexFloatInput


class hclStandardLinkSetupObject(hclConstraintSetSetupObject):
    name: str
    simulationMesh: any
    vertexSelection: hclVertexSelectionInput
    edgeSelection: hclEdgeSelectionInput
    ignoreHiddenEdges: bool
    stiffness: hclVertexFloatInput
    allowedCompression: hclVertexFloatInput
    allowedStretching: hclVertexFloatInput

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.simulationMesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.vertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.edgeSelection = hclEdgeSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.ignoreHiddenEdges = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.stiffness = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.allowedCompression = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.allowedStretching = hclVertexFloatInput(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", simulationMesh={simulationMesh}, vertexSelection={vertexSelection}, edgeSelection={edgeSelection}, ignoreHiddenEdges={ignoreHiddenEdges}, stiffness={stiffness}, allowedCompression={allowedCompression}, allowedStretching={allowedStretching}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "simulationMesh": self.simulationMesh,
            "vertexSelection": self.vertexSelection,
            "edgeSelection": self.edgeSelection,
            "ignoreHiddenEdges": self.ignoreHiddenEdges,
            "stiffness": self.stiffness,
            "allowedCompression": self.allowedCompression,
            "allowedStretching": self.allowedStretching,
        })
