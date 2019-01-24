from .hkReferencedObject import hkReferencedObject
from .common import any
from .hkpStorageExtendedMeshShapeMaterial import hkpStorageExtendedMeshShapeMaterial


class hkpStorageExtendedMeshShapeShapeSubpartStorage(hkReferencedObject):
    materialIndices: any
    materials: hkpStorageExtendedMeshShapeMaterial
    materialIndices16: any
