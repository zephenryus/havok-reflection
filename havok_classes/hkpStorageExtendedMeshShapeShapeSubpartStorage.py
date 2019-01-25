from .hkReferencedObject import hkReferencedObject
from .common import any
from .hkpStorageExtendedMeshShapeMaterial import hkpStorageExtendedMeshShapeMaterial


class hkpStorageExtendedMeshShapeShapeSubpartStorage(hkReferencedObject):
    materialIndices: any
    materials: hkpStorageExtendedMeshShapeMaterial
    materialIndices16: any

    def __init__(self, infile):
        self.materialIndices = any(infile)  # TYPE_ARRAY
        self.materials = hkpStorageExtendedMeshShapeMaterial(infile)  # TYPE_ARRAY
        self.materialIndices16 = any(infile)  # TYPE_ARRAY
