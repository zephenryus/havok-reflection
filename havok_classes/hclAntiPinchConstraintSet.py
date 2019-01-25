from .hclConstraintSet import hclConstraintSet
from typing import List
from .common import get_array
from .hclAntiPinchConstraintSetPerParticle import hclAntiPinchConstraintSetPerParticle
import struct


class hclAntiPinchConstraintSet(hclConstraintSet):
    perParticleData: List[hclAntiPinchConstraintSetPerParticle]
    toAnimPeriod: float
    toSimPeriod: float
    toSimMaxDistance: float
    referenceMeshBufferIdx: int

    def __init__(self, infile):
        self.perParticleData = get_array(infile, hclAntiPinchConstraintSetPerParticle, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.toAnimPeriod = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.toSimPeriod = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.toSimMaxDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.referenceMeshBufferIdx = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} perParticleData=[{perParticleData}], toAnimPeriod={toAnimPeriod}, toSimPeriod={toSimPeriod}, toSimMaxDistance={toSimMaxDistance}, referenceMeshBufferIdx={referenceMeshBufferIdx}>".format(**{
            "class_name": self.__class__.__name__,
            "perParticleData": self.perParticleData,
            "toAnimPeriod": self.toAnimPeriod,
            "toSimPeriod": self.toSimPeriod,
            "toSimMaxDistance": self.toSimMaxDistance,
            "referenceMeshBufferIdx": self.referenceMeshBufferIdx,
        })
