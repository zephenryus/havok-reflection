from .hkResourceHandle import hkResourceHandle
from .hkReferencedObject import hkReferencedObject
from .hkMemoryResourceHandleExternalLink import hkMemoryResourceHandleExternalLink


class hkMemoryResourceHandle(hkResourceHandle):
	variant: hkReferencedObject
	name: any
	references: hkMemoryResourceHandleExternalLink
