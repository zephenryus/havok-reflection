from .hkReferencedObject import hkReferencedObject
from .hkGeometry import hkGeometry
from .hkBitField import hkBitField


class hkaiCuttingGeometryInfo(hkReferencedObject):
    geometry: hkGeometry
    cuttingTriangles: hkBitField
