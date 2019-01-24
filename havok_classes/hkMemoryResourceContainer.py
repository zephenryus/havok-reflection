from .hkResourceContainer import hkResourceContainer
from .hkMemoryResourceContainer import hkMemoryResourceContainer
from .hkMemoryResourceHandle import hkMemoryResourceHandle


class hkMemoryResourceContainer(hkResourceContainer):
    name: str
    parent: hkMemoryResourceContainer
    resourceHandles: hkMemoryResourceHandle
    children: hkMemoryResourceContainer
