from .hclOperator import hclOperator
from .hclMoveParticlesOperatorVertexParticlePair import hclMoveParticlesOperatorVertexParticlePair


class hclMoveParticlesOperator(hclOperator):
	vertexParticlePairs: hclMoveParticlesOperatorVertexParticlePair
	simClothIndex: int
	refBufferIdx: int
