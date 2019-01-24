from .hclOperator import hclOperator
from enum import Enum
from .hclMoveParticlesOperatorVertexParticlePair import hclMoveParticlesOperatorVertexParticlePair


class ForceUpgrade610(Enum):
    HCL_FORCE_UPGRADE610 = 0


class hclMoveParticlesOperator(hclOperator):
    vertexParticlePairs: hclMoveParticlesOperatorVertexParticlePair
    simClothIndex: int
    refBufferIdx: int
