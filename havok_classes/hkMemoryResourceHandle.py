from .hkResourceHandle import hkResourceHandle
from .hkReferencedObject import hkReferencedObject
from .hkMemoryResourceHandleExternalLink import hkMemoryResourceHandleExternalLink


class hkMemoryResourceHandle(hkResourceHandle):
    variant: hkReferencedObject
    name: str
    references: hkMemoryResourceHandleExternalLink

    def __init__(self, infile):
        self.variant = hkReferencedObject(infile)  # TYPE_POINTER
        self.name = struct.unpack('>s', infile.read(0))
        self.references = hkMemoryResourceHandleExternalLink(infile)  # TYPE_ARRAY
