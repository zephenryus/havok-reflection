from .hclOperatorSetupObject import hclOperatorSetupObject
from enum import Enum
from .enums import Direction
from .hclSimClothBufferSetupObject import hclSimClothBufferSetupObject
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclBufferSetupObject import hclBufferSetupObject
import struct


class Direction(Enum):
    SIMULATION_TO_DISPLAY = 0
    DISPLAY_TO_SIMULATION = 1


class hclVertexGatherSetupObject(hclOperatorSetupObject):
    name: str
    direction: Direction
    simulationBuffer: hclSimClothBufferSetupObject
    simulationParticleSelection: hclVertexSelectionInput
    displayBuffer: hclBufferSetupObject
    displayVertexSelection: hclVertexSelectionInput
    gatherAllThreshold: float
    gatherNormals: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.direction = Direction(infile)  # TYPE_ENUM
        self.simulationBuffer = hclSimClothBufferSetupObject(infile)  # TYPE_POINTER
        self.simulationParticleSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.displayBuffer = hclBufferSetupObject(infile)  # TYPE_POINTER
        self.displayVertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.gatherAllThreshold = struct.unpack('>f', infile.read(4))
        self.gatherNormals = struct.unpack('>?', infile.read(1))
