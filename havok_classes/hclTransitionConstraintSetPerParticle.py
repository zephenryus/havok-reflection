import struct


class hclTransitionConstraintSetPerParticle(object):
    particleIndex: int
    referenceVertex: int
    toAnimDelay: float
    toSimDelay: float
    toSimMaxDistance: float

    def __init__(self, infile):
        self.particleIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.referenceVertex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.toAnimDelay = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.toSimDelay = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.toSimMaxDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} particleIndex={particleIndex}, referenceVertex={referenceVertex}, toAnimDelay={toAnimDelay}, toSimDelay={toSimDelay}, toSimMaxDistance={toSimMaxDistance}>".format(**{
            "class_name": self.__class__.__name__,
            "particleIndex": self.particleIndex,
            "referenceVertex": self.referenceVertex,
            "toAnimDelay": self.toAnimDelay,
            "toSimDelay": self.toSimDelay,
            "toSimMaxDistance": self.toSimMaxDistance,
        })
