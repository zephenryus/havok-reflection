from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
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
