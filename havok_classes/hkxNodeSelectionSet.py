from .hkxAttributeHolder import hkxAttributeHolder
from .hkxNode import hkxNode


class hkxNodeSelectionSet(hkxAttributeHolder):
    selectedNodes: hkxNode
    name: str

    def __init__(self, infile):
        self.selectedNodes = hkxNode(infile)  # TYPE_ARRAY
        self.name = struct.unpack('>s', infile.read(0))
