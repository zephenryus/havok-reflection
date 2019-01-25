import struct


class hclLocalRangeConstraintSetLocalConstraint(object):
    particleIndex: int
    referenceVertex: int
    maximumDistance: float
    maxNormalDistance: float
    minNormalDistance: float

    def __init__(self, infile):
        self.particleIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.referenceVertex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.maximumDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxNormalDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.minNormalDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} particleIndex={particleIndex}, referenceVertex={referenceVertex}, maximumDistance={maximumDistance}, maxNormalDistance={maxNormalDistance}, minNormalDistance={minNormalDistance}>".format(**{
            "class_name": self.__class__.__name__,
            "particleIndex": self.particleIndex,
            "referenceVertex": self.referenceVertex,
            "maximumDistance": self.maximumDistance,
            "maxNormalDistance": self.maxNormalDistance,
            "minNormalDistance": self.minNormalDistance,
        })
