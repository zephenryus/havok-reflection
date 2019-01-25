from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkpStorageExtendedMeshShapeMaterial import hkpStorageExtendedMeshShapeMaterial
from .hkpNamedMeshMaterial import hkpNamedMeshMaterial


class hkpStorageExtendedMeshShapeMeshSubpartStorage(hkReferencedObject):
    vertices: List[vector4]
    indices8: List[int]
    indices16: List[int]
    indices32: List[int]
    materialIndices: List[int]
    materials: List[hkpStorageExtendedMeshShapeMaterial]
    namedMaterials: List[hkpNamedMeshMaterial]
    materialIndices16: List[int]

    def __init__(self, infile):
        self.vertices = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.indices8 = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.indices16 = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.indices32 = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.materialIndices = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.materials = get_array(infile, hkpStorageExtendedMeshShapeMaterial, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.namedMaterials = get_array(infile, hkpNamedMeshMaterial, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.materialIndices16 = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16

    def __repr__(self):
        return "<{class_name} vertices=[{vertices}], indices8=[{indices8}], indices16=[{indices16}], indices32=[{indices32}], materialIndices=[{materialIndices}], materials=[{materials}], namedMaterials=[{namedMaterials}], materialIndices16=[{materialIndices16}]>".format(**{
            "class_name": self.__class__.__name__,
            "vertices": self.vertices,
            "indices8": self.indices8,
            "indices16": self.indices16,
            "indices32": self.indices32,
            "materialIndices": self.materialIndices,
            "materials": self.materials,
            "namedMaterials": self.namedMaterials,
            "materialIndices16": self.materialIndices16,
        })
