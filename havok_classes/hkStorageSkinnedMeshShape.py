from .hkSkinnedMeshShape import hkSkinnedMeshShape
from typing import List
from .common import get_array
from .hkSkinnedMeshShapeBoneSet import hkSkinnedMeshShapeBoneSet
from .hkSkinnedMeshShapeBoneSection import hkSkinnedMeshShapeBoneSection
from .hkSkinnedMeshShapePart import hkSkinnedMeshShapePart


class hkStorageSkinnedMeshShape(hkSkinnedMeshShape):
    bonesBuffer: List[int]
    boneSets: List[hkSkinnedMeshShapeBoneSet]
    boneSections: List[hkSkinnedMeshShapeBoneSection]
    parts: List[hkSkinnedMeshShapePart]
    name: str

    def __init__(self, infile):
        self.bonesBuffer = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_INT16
        self.boneSets = get_array(infile, hkSkinnedMeshShapeBoneSet, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.boneSections = get_array(infile, hkSkinnedMeshShapeBoneSection, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.parts = get_array(infile, hkSkinnedMeshShapePart, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} bonesBuffer=[{bonesBuffer}], boneSets=[{boneSets}], boneSections=[{boneSections}], parts=[{parts}], name=\"{name}\">".format(**{
            "class_name": self.__class__.__name__,
            "bonesBuffer": self.bonesBuffer,
            "boneSets": self.boneSets,
            "boneSections": self.boneSections,
            "parts": self.parts,
            "name": self.name,
        })
