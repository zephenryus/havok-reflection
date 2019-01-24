from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
from .hclBufferSetupObject import hclBufferSetupObject


class hclTransitionSetupObject(hclConstraintSetSetupObject):
    name: str
    simulationMesh: hclSimulationSetupMesh
    vertexSelection: hclVertexSelectionInput
    toAnimDelay: hclVertexFloatInput
    toSimDelay: hclVertexFloatInput
    toSimMaxDistance: hclVertexFloatInput
    toAnimPeriod: float
    toSimPeriod: float
    referenceBufferSetup: hclBufferSetupObject
