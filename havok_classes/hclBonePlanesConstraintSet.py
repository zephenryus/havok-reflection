from .hclConstraintSet import hclConstraintSet
from .hclBonePlanesConstraintSetBonePlane import hclBonePlanesConstraintSetBonePlane
import struct


class hclBonePlanesConstraintSet(hclConstraintSet):
    bonePlanes: hclBonePlanesConstraintSetBonePlane
    transformSetIndex: int

    def __init__(self, infile):
        self.bonePlanes = hclBonePlanesConstraintSetBonePlane(infile)  # TYPE_ARRAY
        self.transformSetIndex = struct.unpack('>I', infile.read(4))
