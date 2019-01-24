from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclBufferSetupObject import hclBufferSetupObject
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
from .enums import ShapeType


class hclLocalRangeSetupObject(hclConstraintSetSetupObject):
    name: str
    simulationMesh: hclSimulationSetupMesh
    referenceBufferSetup: hclBufferSetupObject
    vertexSelection: hclVertexSelectionInput
    maximumDistance: hclVertexFloatInput
    minNormalDistance: hclVertexFloatInput
    maxNormalDistance: hclVertexFloatInput
    stiffness: float
    localRangeShape: ShapeType
    useMinNormalDistance: bool
    useMaxNormalDistance: bool
