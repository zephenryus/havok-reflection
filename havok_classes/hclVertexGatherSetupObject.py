from .hclOperatorSetupObject import hclOperatorSetupObject
from enum import Enum
from .enums import Direction
from .hclSimClothBufferSetupObject import hclSimClothBufferSetupObject
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclBufferSetupObject import hclBufferSetupObject


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
