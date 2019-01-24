from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclEdgeSelectionInput import hclEdgeSelectionInput
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
