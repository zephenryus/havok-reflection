from .hkMeshShape import hkMeshShape
from .hkMemoryMeshShapeSection import hkMemoryMeshShapeSection


class hkMemoryMeshShape(hkMeshShape):
	sections: hkMemoryMeshShapeSection
	indices16: any
	indices32: any
	name: any
