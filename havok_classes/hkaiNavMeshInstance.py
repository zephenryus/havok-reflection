from .hkReferencedObject import hkReferencedObject
from .hkaiNavMesh import hkaiNavMesh
from .hkaiReferenceFrame import hkaiReferenceFrame
from .hkaiNavMeshFace import hkaiNavMeshFace
from .hkaiNavMeshEdge import hkaiNavMeshEdge
from .hkaiNavMeshFace import hkaiNavMeshFace
from .hkaiNavMeshEdge import hkaiNavMeshEdge
from .hkaiNavMeshClearanceCache import hkaiNavMeshClearanceCache


class hkaiNavMeshInstance(hkReferencedObject):
	originalFaces: any
	originalEdges: any
	originalVertices: any
	originalFaceData: any
	faceDataStriding: int
	originalEdgeData: any
	edgeDataStriding: int
	originalMesh: hkaiNavMesh
	referenceFrame: hkaiReferenceFrame
	edgeMap: any
	faceMap: any
	instancedFaces: hkaiNavMeshFace
	instancedEdges: hkaiNavMeshEdge
	ownedFaces: hkaiNavMeshFace
	ownedEdges: hkaiNavMeshEdge
	ownedVertices: any
	faceFlags: any
	cuttingInfo: any
	instancedFaceData: any
	instancedEdgeData: any
	ownedFaceData: any
	ownedEdgeData: any
	sectionUid: int
	runtimeId: int
	layer: int
	clearanceCaches: hkaiNavMeshClearanceCache
