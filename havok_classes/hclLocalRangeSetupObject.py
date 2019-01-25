from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclBufferSetupObject import hclBufferSetupObject
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
import struct
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

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.simulationMesh = hclSimulationSetupMesh(infile)  # TYPE_POINTER
        self.referenceBufferSetup = hclBufferSetupObject(infile)  # TYPE_POINTER
        self.vertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.maximumDistance = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.minNormalDistance = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.maxNormalDistance = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.stiffness = struct.unpack('>f', infile.read(4))
        self.localRangeShape = ShapeType(infile)  # TYPE_ENUM
        self.useMinNormalDistance = struct.unpack('>?', infile.read(1))
        self.useMaxNormalDistance = struct.unpack('>?', infile.read(1))
