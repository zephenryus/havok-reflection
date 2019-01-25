from .hclConstraintSetSetupObject import hclConstraintSetSetupObject
from .hclSimulationSetupMesh import hclSimulationSetupMesh
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
import struct
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

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.simulationMesh = hclSimulationSetupMesh(infile)  # TYPE_POINTER
        self.vertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.toAnimDelay = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.toSimDelay = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.toSimMaxDistance = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.toAnimPeriod = struct.unpack('>f', infile.read(4))
        self.toSimPeriod = struct.unpack('>f', infile.read(4))
        self.referenceBufferSetup = hclBufferSetupObject(infile)  # TYPE_POINTER
