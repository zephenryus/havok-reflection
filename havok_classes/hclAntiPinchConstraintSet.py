from .hclConstraintSet import hclConstraintSet
from .hclAntiPinchConstraintSetPerParticle import hclAntiPinchConstraintSetPerParticle
import struct


class hclAntiPinchConstraintSet(hclConstraintSet):
    perParticleData: hclAntiPinchConstraintSetPerParticle
    toAnimPeriod: float
    toSimPeriod: float
    toSimMaxDistance: float
    referenceMeshBufferIdx: int

    def __init__(self, infile):
        self.perParticleData = hclAntiPinchConstraintSetPerParticle(infile)  # TYPE_ARRAY
        self.toAnimPeriod = struct.unpack('>f', infile.read(4))
        self.toSimPeriod = struct.unpack('>f', infile.read(4))
        self.toSimMaxDistance = struct.unpack('>f', infile.read(4))
        self.referenceMeshBufferIdx = struct.unpack('>I', infile.read(4))
