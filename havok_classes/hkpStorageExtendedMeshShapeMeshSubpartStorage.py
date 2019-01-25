from .hkReferencedObject import hkReferencedObject
from .common import any
from .hkpStorageExtendedMeshShapeMaterial import hkpStorageExtendedMeshShapeMaterial
from .hkpNamedMeshMaterial import hkpNamedMeshMaterial


class hkpStorageExtendedMeshShapeMeshSubpartStorage(hkReferencedObject):
    vertices: any
    indices8: any
    indices16: any
    indices32: any
    materialIndices: any
    materials: hkpStorageExtendedMeshShapeMaterial
    namedMaterials: hkpNamedMeshMaterial
    materialIndices16: any

    def __init__(self, infile):
        self.vertices = any(infile)  # TYPE_ARRAY
        self.indices8 = any(infile)  # TYPE_ARRAY
        self.indices16 = any(infile)  # TYPE_ARRAY
        self.indices32 = any(infile)  # TYPE_ARRAY
        self.materialIndices = any(infile)  # TYPE_ARRAY
        self.materials = hkpStorageExtendedMeshShapeMaterial(infile)  # TYPE_ARRAY
        self.namedMaterials = hkpNamedMeshMaterial(infile)  # TYPE_ARRAY
        self.materialIndices16 = any(infile)  # TYPE_ARRAY
