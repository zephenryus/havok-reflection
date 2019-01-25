from .hkResourceContainer import hkResourceContainer
from .hkMemoryResourceContainer import hkMemoryResourceContainer
from typing import List
from .common import get_array
from .hkMemoryResourceHandle import hkMemoryResourceHandle


class hkMemoryResourceContainer(hkResourceContainer):
    name: str
    parent: any
    resourceHandles: List[hkMemoryResourceHandle]
    children: List[hkMemoryResourceContainer]

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.parent = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.resourceHandles = get_array(infile, hkMemoryResourceHandle, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.children = get_array(infile, hkMemoryResourceContainer, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} name=\"{name}\", parent={parent}, resourceHandles=[{resourceHandles}], children=[{children}]>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "parent": self.parent,
            "resourceHandles": self.resourceHandles,
            "children": self.children,
        })
