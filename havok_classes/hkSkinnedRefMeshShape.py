from .hkMeshShape import hkMeshShape
from .hkSkinnedMeshShape import hkSkinnedMeshShape


class hkSkinnedRefMeshShape(hkMeshShape):
	skinnedMeshShape: hkSkinnedMeshShape
	bones: any
	localFromRootTransforms: any
	name: any
