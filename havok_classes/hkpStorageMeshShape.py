from .hkpMeshShape import hkpMeshShape
from typing import List
from .common import get_array
from .hkpStorageMeshShapeSubpartStorage import hkpStorageMeshShapeSubpartStorage


class hkpStorageMeshShape(hkpMeshShape):
    storage: List[hkpStorageMeshShapeSubpartStorage]

    def __init__(self, infile):
        self.storage = get_array(infile, hkpStorageMeshShapeSubpartStorage, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} storage=[{storage}]>".format(**{
            "class_name": self.__class__.__name__,
            "storage": self.storage,
        })
