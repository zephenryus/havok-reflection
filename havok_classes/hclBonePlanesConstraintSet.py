from .hclConstraintSet import hclConstraintSet
from typing import List
from .common import get_array
from .hclBonePlanesConstraintSetBonePlane import hclBonePlanesConstraintSetBonePlane
import struct


class hclBonePlanesConstraintSet(hclConstraintSet):
    bonePlanes: List[hclBonePlanesConstraintSetBonePlane]
    transformSetIndex: int

    def __init__(self, infile):
        self.bonePlanes = get_array(infile, hclBonePlanesConstraintSetBonePlane, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.transformSetIndex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} bonePlanes=[{bonePlanes}], transformSetIndex={transformSetIndex}>".format(**{
            "class_name": self.__class__.__name__,
            "bonePlanes": self.bonePlanes,
            "transformSetIndex": self.transformSetIndex,
        })
