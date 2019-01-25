from .hclOperator import hclOperator
from enum import Enum
from typing import List
from .common import get_array
from .hclMoveParticlesOperatorVertexParticlePair import hclMoveParticlesOperatorVertexParticlePair
import struct


class ForceUpgrade610(Enum):
    HCL_FORCE_UPGRADE610 = 0


class hclMoveParticlesOperator(hclOperator):
    vertexParticlePairs: List[hclMoveParticlesOperatorVertexParticlePair]
    simClothIndex: int
    refBufferIdx: int

    def __init__(self, infile):
        self.vertexParticlePairs = get_array(infile, hclMoveParticlesOperatorVertexParticlePair, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.simClothIndex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.refBufferIdx = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} vertexParticlePairs=[{vertexParticlePairs}], simClothIndex={simClothIndex}, refBufferIdx={refBufferIdx}>".format(**{
            "class_name": self.__class__.__name__,
            "vertexParticlePairs": self.vertexParticlePairs,
            "simClothIndex": self.simClothIndex,
            "refBufferIdx": self.refBufferIdx,
        })
