from .hkResourceContainer import hkResourceContainer
from .hkMemoryResourceContainer import hkMemoryResourceContainer
from .hkMemoryResourceHandle import hkMemoryResourceHandle


class hkMemoryResourceContainer(hkResourceContainer):
    name: str
    parent: hkMemoryResourceContainer
    resourceHandles: hkMemoryResourceHandle
    children: hkMemoryResourceContainer

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.parent = hkMemoryResourceContainer(infile)  # TYPE_POINTER
        self.resourceHandles = hkMemoryResourceHandle(infile)  # TYPE_ARRAY
        self.children = hkMemoryResourceContainer(infile)  # TYPE_ARRAY
