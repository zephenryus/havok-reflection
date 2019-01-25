from .hclConstraintSet import hclConstraintSet
from .hclTransitionConstraintSetPerParticle import hclTransitionConstraintSetPerParticle
import struct


class hclTransitionConstraintSet(hclConstraintSet):
    perParticleData: hclTransitionConstraintSetPerParticle
    toAnimPeriod: float
    toAnimPlusDelayPeriod: float
    toSimPeriod: float
    toSimPlusDelayPeriod: float
    referenceMeshBufferIdx: int

    def __init__(self, infile):
        self.perParticleData = hclTransitionConstraintSetPerParticle(infile)  # TYPE_ARRAY
        self.toAnimPeriod = struct.unpack('>f', infile.read(4))
        self.toAnimPlusDelayPeriod = struct.unpack('>f', infile.read(4))
        self.toSimPeriod = struct.unpack('>f', infile.read(4))
        self.toSimPlusDelayPeriod = struct.unpack('>f', infile.read(4))
        self.referenceMeshBufferIdx = struct.unpack('>I', infile.read(4))
