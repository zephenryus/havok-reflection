from .hkReferencedObject import hkReferencedObject
from .hkpStorageExtendedMeshShapeMaterial import hkpStorageExtendedMeshShapeMaterial
from .hkpNamedMeshMaterial import hkpNamedMeshMaterial


class hkpStorageExtendedMeshShapeMeshSubpartStorage(hkReferencedObject):
	vertices: any
	indices8: any
	indices16: any
	indices32: any
	materialIndices: any
	materials: hkpStorageExtendedMeshShapeMaterial
	namedMaterials: hkpNamedMeshMaterial
	materialIndices16: any
