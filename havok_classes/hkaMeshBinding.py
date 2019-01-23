from .hkReferencedObject import hkReferencedObject
from .hkxMesh import hkxMesh
from .hkaSkeleton import hkaSkeleton
from .hkaMeshBindingMapping import hkaMeshBindingMapping


class hkaMeshBinding(hkReferencedObject):
	mesh: hkxMesh
	originalSkeletonName: any
	name: any
	skeleton: hkaSkeleton
	mappings: hkaMeshBindingMapping
	boneFromSkinMeshTransforms: any
