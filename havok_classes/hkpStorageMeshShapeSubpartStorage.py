from .hkReferencedObject import hkReferencedObject
from .common import any


class hkpStorageMeshShapeSubpartStorage(hkReferencedObject):
    vertices: any
    indices16: any
    indices32: any
    materialIndices: any
    materials: any
    materialIndices16: any

    def __init__(self, infile):
        self.vertices = any(infile)  # TYPE_ARRAY
        self.indices16 = any(infile)  # TYPE_ARRAY
        self.indices32 = any(infile)  # TYPE_ARRAY
        self.materialIndices = any(infile)  # TYPE_ARRAY
        self.materials = any(infile)  # TYPE_ARRAY
        self.materialIndices16 = any(infile)  # TYPE_ARRAY
