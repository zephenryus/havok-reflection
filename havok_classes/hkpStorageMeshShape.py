from .hkpMeshShape import hkpMeshShape
from .hkpStorageMeshShapeSubpartStorage import hkpStorageMeshShapeSubpartStorage


class hkpStorageMeshShape(hkpMeshShape):
    storage: hkpStorageMeshShapeSubpartStorage

    def __init__(self, infile):
        self.storage = hkpStorageMeshShapeSubpartStorage(infile)  # TYPE_ARRAY
