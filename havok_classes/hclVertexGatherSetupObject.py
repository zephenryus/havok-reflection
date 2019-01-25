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
    simulationBuffer: any
    simulationParticleSelection: hclVertexSelectionInput
    displayBuffer: any
    displayVertexSelection: hclVertexSelectionInput
    gatherAllThreshold: float
    gatherNormals: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.direction = Direction(infile)  # TYPE_ENUM:TYPE_UINT32
        self.simulationBuffer = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.simulationParticleSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.displayBuffer = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.displayVertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.gatherAllThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.gatherNormals = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", direction={direction}, simulationBuffer={simulationBuffer}, simulationParticleSelection={simulationParticleSelection}, displayBuffer={displayBuffer}, displayVertexSelection={displayVertexSelection}, gatherAllThreshold={gatherAllThreshold}, gatherNormals={gatherNormals}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "direction": self.direction,
            "simulationBuffer": self.simulationBuffer,
            "simulationParticleSelection": self.simulationParticleSelection,
            "displayBuffer": self.displayBuffer,
            "displayVertexSelection": self.displayVertexSelection,
            "gatherAllThreshold": self.gatherAllThreshold,
            "gatherNormals": self.gatherNormals,
        })
