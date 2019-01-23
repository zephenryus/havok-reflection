from .hkReferencedObject import hkReferencedObject
from .hkMeshBoneIndexMapping import hkMeshBoneIndexMapping


class hkIndexedTransformSet(hkReferencedObject):
	matrices: any
	inverseMatrices: any
	matricesOrder: any
	matricesNames: any
	indexMappings: hkMeshBoneIndexMapping
	allMatricesAreAffine: bool
