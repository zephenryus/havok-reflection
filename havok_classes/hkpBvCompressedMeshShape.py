from .hkpBvTreeShape import hkpBvTreeShape
from .hkpBvCompressedMeshShapeTree import hkpBvCompressedMeshShapeTree


class hkpBvCompressedMeshShape(hkpBvTreeShape):
	convexRadius: float
	weldingType: any
	hasPerPrimitiveCollisionFilterInfo: bool
	hasPerPrimitiveUserData: bool
	collisionFilterInfoPalette: any
	userDataPalette: any
	userStringPalette: any
	tree: hkpBvCompressedMeshShapeTree
