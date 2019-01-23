from .hkReferencedObject import hkReferencedObject
from .hkaiNavMeshFace import hkaiNavMeshFace
from .hkaiNavMeshEdge import hkaiNavMeshEdge
from .hkaiStreamingSet import hkaiStreamingSet
from .hkAabb import hkAabb


class hkaiNavMesh(hkReferencedObject):
	faces: hkaiNavMeshFace
	edges: hkaiNavMeshEdge
	vertices: any
	streamingSets: hkaiStreamingSet
	faceData: any
	edgeData: any
	faceDataStriding: int
	edgeDataStriding: int
	flags: int
	aabb: hkAabb
	erosionRadius: float
	userData: int
