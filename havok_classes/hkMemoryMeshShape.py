from .hkMeshShape import hkMeshShape
from typing import List
from .common import get_array
from .hkMemoryMeshShapeSection import hkMemoryMeshShapeSection


class hkMemoryMeshShape(hkMeshShape):
    sections: List[hkMemoryMeshShapeSection]
    indices16: List[int]
    indices32: List[int]
    name: str

    def __init__(self, infile):
        self.sections = get_array(infile, hkMemoryMeshShapeSection, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.indices16 = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.indices32 = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} sections=[{sections}], indices16=[{indices16}], indices32=[{indices32}], name=\"{name}\">".format(**{
            "class_name": self.__class__.__name__,
            "sections": self.sections,
            "indices16": self.indices16,
            "indices32": self.indices32,
            "name": self.name,
        })
