from .hkResourceContainer import hkResourceContainer
from .hkMemoryResourceContainer import hkMemoryResourceContainer
from .hkMemoryResourceHandle import hkMemoryResourceHandle
from .hkMemoryResourceContainer import hkMemoryResourceContainer


class hkMemoryResourceContainer(hkResourceContainer):
	name: any
	parent: hkMemoryResourceContainer
	resourceHandles: hkMemoryResourceHandle
	children: hkMemoryResourceContainer
