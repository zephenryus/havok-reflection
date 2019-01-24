from .hkReferencedObject import hkReferencedObject
from .hkxMesh import hkxMesh
from .common import any


class hkxSkinBinding(hkReferencedObject):
    mesh: hkxMesh
    nodeNames: any
    bindPose: any
    initSkinTransform: any
