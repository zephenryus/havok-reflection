from .hkReferencedObject import hkReferencedObject
from .hkxMesh import hkxMesh
from .common import any


class hkxSkinBinding(hkReferencedObject):
    mesh: hkxMesh
    nodeNames: any
    bindPose: any
    initSkinTransform: any

    def __init__(self, infile):
        self.mesh = hkxMesh(infile)  # TYPE_POINTER
        self.nodeNames = any(infile)  # TYPE_ARRAY
        self.bindPose = any(infile)  # TYPE_ARRAY
        self.initSkinTransform = any(infile)  # TYPE_MATRIX4
