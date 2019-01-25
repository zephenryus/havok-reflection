from .hclConstraintSet import hclConstraintSet
from typing import List
from .common import get_array
from .hclTransitionConstraintSetPerParticle import hclTransitionConstraintSetPerParticle
import struct


class hclTransitionConstraintSet(hclConstraintSet):
    perParticleData: List[hclTransitionConstraintSetPerParticle]
    toAnimPeriod: float
    toAnimPlusDelayPeriod: float
    toSimPeriod: float
    toSimPlusDelayPeriod: float
    referenceMeshBufferIdx: int

    def __init__(self, infile):
        self.perParticleData = get_array(infile, hclTransitionConstraintSetPerParticle, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.toAnimPeriod = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.toAnimPlusDelayPeriod = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.toSimPeriod = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.toSimPlusDelayPeriod = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.referenceMeshBufferIdx = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} perParticleData=[{perParticleData}], toAnimPeriod={toAnimPeriod}, toAnimPlusDelayPeriod={toAnimPlusDelayPeriod}, toSimPeriod={toSimPeriod}, toSimPlusDelayPeriod={toSimPlusDelayPeriod}, referenceMeshBufferIdx={referenceMeshBufferIdx}>".format(**{
            "class_name": self.__class__.__name__,
            "perParticleData": self.perParticleData,
            "toAnimPeriod": self.toAnimPeriod,
            "toAnimPlusDelayPeriod": self.toAnimPlusDelayPeriod,
            "toSimPeriod": self.toSimPeriod,
            "toSimPlusDelayPeriod": self.toSimPlusDelayPeriod,
            "referenceMeshBufferIdx": self.referenceMeshBufferIdx,
        })
