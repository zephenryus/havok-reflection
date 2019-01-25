from .hkpExtendedMeshShape import hkpExtendedMeshShape
from .hkpStorageExtendedMeshShapeMeshSubpartStorage import hkpStorageExtendedMeshShapeMeshSubpartStorage
from .hkpStorageExtendedMeshShapeShapeSubpartStorage import hkpStorageExtendedMeshShapeShapeSubpartStorage


class hkpStorageExtendedMeshShape(hkpExtendedMeshShape):
    meshstorage: hkpStorageExtendedMeshShapeMeshSubpartStorage
    shapestorage: hkpStorageExtendedMeshShapeShapeSubpartStorage

    def __init__(self, infile):
        self.meshstorage = hkpStorageExtendedMeshShapeMeshSubpartStorage(infile)  # TYPE_ARRAY
        self.shapestorage = hkpStorageExtendedMeshShapeShapeSubpartStorage(infile)  # TYPE_ARRAY
