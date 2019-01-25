from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkpStorageExtendedMeshShapeMaterial import hkpStorageExtendedMeshShapeMaterial


class hkpStorageExtendedMeshShapeShapeSubpartStorage(hkReferencedObject):
    materialIndices: List[int]
    materials: List[hkpStorageExtendedMeshShapeMaterial]
    materialIndices16: List[int]

    def __init__(self, infile):
        self.materialIndices = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.materials = get_array(infile, hkpStorageExtendedMeshShapeMaterial, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.materialIndices16 = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16

    def __repr__(self):
        return "<{class_name} materialIndices=[{materialIndices}], materials=[{materials}], materialIndices16=[{materialIndices16}]>".format(**{
            "class_name": self.__class__.__name__,
            "materialIndices": self.materialIndices,
            "materials": self.materials,
            "materialIndices16": self.materialIndices16,
        })
