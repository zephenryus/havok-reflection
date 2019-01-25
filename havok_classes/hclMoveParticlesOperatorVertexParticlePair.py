import struct


class hclMoveParticlesOperatorVertexParticlePair(object):
    vertexIndex: int
    particleIndex: int

    def __init__(self, infile):
        self.vertexIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.particleIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} vertexIndex={vertexIndex}, particleIndex={particleIndex}>".format(**{
            "class_name": self.__class__.__name__,
            "vertexIndex": self.vertexIndex,
            "particleIndex": self.particleIndex,
        })
