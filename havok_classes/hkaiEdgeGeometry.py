from .hkReferencedObject import hkReferencedObject
from .hkaiEdgeGeometryEdge import hkaiEdgeGeometryEdge
from .hkaiEdgeGeometryFace import hkaiEdgeGeometryFace
from .hkaiEdgeGeometryFace import hkaiEdgeGeometryFace


class hkaiEdgeGeometry(hkReferencedObject):
	edges: hkaiEdgeGeometryEdge
	faces: hkaiEdgeGeometryFace
	vertices: any
	zeroFace: hkaiEdgeGeometryFace
