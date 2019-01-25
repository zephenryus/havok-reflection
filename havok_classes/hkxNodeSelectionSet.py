from .hkxAttributeHolder import hkxAttributeHolder
from typing import List
from .common import get_array
from .hkxNode import hkxNode


class hkxNodeSelectionSet(hkxAttributeHolder):
    selectedNodes: List[hkxNode]
    name: str

    def __init__(self, infile):
        self.selectedNodes = get_array(infile, hkxNode, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} selectedNodes=[{selectedNodes}], name=\"{name}\">".format(**{
            "class_name": self.__class__.__name__,
            "selectedNodes": self.selectedNodes,
            "name": self.name,
        })
