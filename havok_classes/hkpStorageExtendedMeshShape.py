from .hkpExtendedMeshShape import hkpExtendedMeshShape
from typing import List
from .common import get_array
from .hkpStorageExtendedMeshShapeMeshSubpartStorage import hkpStorageExtendedMeshShapeMeshSubpartStorage
from .hkpStorageExtendedMeshShapeShapeSubpartStorage import hkpStorageExtendedMeshShapeShapeSubpartStorage


class hkpStorageExtendedMeshShape(hkpExtendedMeshShape):
    meshstorage: List[hkpStorageExtendedMeshShapeMeshSubpartStorage]
    shapestorage: List[hkpStorageExtendedMeshShapeShapeSubpartStorage]

    def __init__(self, infile):
        self.meshstorage = get_array(infile, hkpStorageExtendedMeshShapeMeshSubpartStorage, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.shapestorage = get_array(infile, hkpStorageExtendedMeshShapeShapeSubpartStorage, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} meshstorage=[{meshstorage}], shapestorage=[{shapestorage}]>".format(**{
            "class_name": self.__class__.__name__,
            "meshstorage": self.meshstorage,
            "shapestorage": self.shapestorage,
        })
