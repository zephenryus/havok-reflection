import struct


class hclAntiPinchConstraintSetPerParticle(object):
    particleIndex: int
    referenceVertex: int

    def __init__(self, infile):
        self.particleIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.referenceVertex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} particleIndex={particleIndex}, referenceVertex={referenceVertex}>".format(**{
            "class_name": self.__class__.__name__,
            "particleIndex": self.particleIndex,
            "referenceVertex": self.referenceVertex,
        })
