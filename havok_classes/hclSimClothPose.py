from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array


class hclSimClothPose(hkReferencedObject):
    name: str
    positions: List[vector4]

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.positions = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4

    def __repr__(self):
        return "<{class_name} name=\"{name}\", positions=[{positions}]>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "positions": self.positions,
        })
