from .hkReferencedObject import hkReferencedObject
from .hkxMesh import hkxMesh


class hkxSkinBinding(hkReferencedObject):
	mesh: hkxMesh
	nodeNames: any
	bindPose: any
	initSkinTransform: any
