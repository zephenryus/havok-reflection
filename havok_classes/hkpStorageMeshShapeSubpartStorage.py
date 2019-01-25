from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array


class hkpStorageMeshShapeSubpartStorage(hkReferencedObject):
    vertices: List[float]
    indices16: List[int]
    indices32: List[int]
    materialIndices: List[int]
    materials: List[int]
    materialIndices16: List[int]

    def __init__(self, infile):
        self.vertices = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.indices16 = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.indices32 = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.materialIndices = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.materials = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.materialIndices16 = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16

    def __repr__(self):
        return "<{class_name} vertices=[{vertices}], indices16=[{indices16}], indices32=[{indices32}], materialIndices=[{materialIndices}], materials=[{materials}], materialIndices16=[{materialIndices16}]>".format(**{
            "class_name": self.__class__.__name__,
            "vertices": self.vertices,
            "indices16": self.indices16,
            "indices32": self.indices32,
            "materialIndices": self.materialIndices,
            "materials": self.materials,
            "materialIndices16": self.materialIndices16,
        })
