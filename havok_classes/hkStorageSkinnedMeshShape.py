from .hkSkinnedMeshShape import hkSkinnedMeshShape
from .hkSkinnedMeshShapeBoneSet import hkSkinnedMeshShapeBoneSet
from .hkSkinnedMeshShapeBoneSection import hkSkinnedMeshShapeBoneSection
from .hkSkinnedMeshShapePart import hkSkinnedMeshShapePart


class hkStorageSkinnedMeshShape(hkSkinnedMeshShape):
	bonesBuffer: any
	boneSets: hkSkinnedMeshShapeBoneSet
	boneSections: hkSkinnedMeshShapeBoneSection
	parts: hkSkinnedMeshShapePart
	name: any
