from .hclOperator import hclOperator
from enum import Enum
from .hclMoveParticlesOperatorVertexParticlePair import hclMoveParticlesOperatorVertexParticlePair
import struct


class ForceUpgrade610(Enum):
    HCL_FORCE_UPGRADE610 = 0


class hclMoveParticlesOperator(hclOperator):
    vertexParticlePairs: hclMoveParticlesOperatorVertexParticlePair
    simClothIndex: int
    refBufferIdx: int

    def __init__(self, infile):
        self.vertexParticlePairs = hclMoveParticlesOperatorVertexParticlePair(infile)  # TYPE_ARRAY
        self.simClothIndex = struct.unpack('>I', infile.read(4))
        self.refBufferIdx = struct.unpack('>I', infile.read(4))
