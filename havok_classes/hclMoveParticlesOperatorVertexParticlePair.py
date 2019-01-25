import struct


class hclMoveParticlesOperatorVertexParticlePair(object):
    vertexIndex: int
    particleIndex: int

    def __init__(self, infile):
        self.vertexIndex = struct.unpack('>H', infile.read(2))
        self.particleIndex = struct.unpack('>H', infile.read(2))
