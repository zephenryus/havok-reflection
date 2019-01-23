from .hkReferencedObject import hkReferencedObject
from .hkGeometryTriangle import hkGeometryTriangle


class hkGeometry(hkReferencedObject):
	vertices: any
	triangles: hkGeometryTriangle
