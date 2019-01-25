from .hkResourceHandle import hkResourceHandle
from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkMemoryResourceHandleExternalLink import hkMemoryResourceHandleExternalLink


class hkMemoryResourceHandle(hkResourceHandle):
    variant: any
    name: str
    references: List[hkMemoryResourceHandleExternalLink]

    def __init__(self, infile):
        self.variant = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.references = get_array(infile, hkMemoryResourceHandleExternalLink, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} variant={variant}, name=\"{name}\", references=[{references}]>".format(**{
            "class_name": self.__class__.__name__,
            "variant": self.variant,
            "name": self.name,
            "references": self.references,
        })
