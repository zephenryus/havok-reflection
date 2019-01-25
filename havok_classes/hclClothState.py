from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hclClothStateBufferAccess import hclClothStateBufferAccess
from .hclClothStateTransformSetAccess import hclClothStateTransformSetAccess


class hclClothState(hkReferencedObject):
    name: str
    operators: List[int]
    usedBuffers: List[hclClothStateBufferAccess]
    usedTransformSets: List[hclClothStateTransformSetAccess]
    usedSimCloths: List[int]

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.operators = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.usedBuffers = get_array(infile, hclClothStateBufferAccess, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.usedTransformSets = get_array(infile, hclClothStateTransformSetAccess, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.usedSimCloths = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32

    def __repr__(self):
        return "<{class_name} name=\"{name}\", operators=[{operators}], usedBuffers=[{usedBuffers}], usedTransformSets=[{usedTransformSets}], usedSimCloths=[{usedSimCloths}]>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "operators": self.operators,
            "usedBuffers": self.usedBuffers,
            "usedTransformSets": self.usedTransformSets,
            "usedSimCloths": self.usedSimCloths,
        })
