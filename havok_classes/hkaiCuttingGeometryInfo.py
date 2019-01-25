from .hkReferencedObject import hkReferencedObject
from .hkGeometry import hkGeometry
from .hkBitField import hkBitField


class hkaiCuttingGeometryInfo(hkReferencedObject):
    geometry: hkGeometry
    cuttingTriangles: hkBitField

    def __init__(self, infile):
        self.geometry = hkGeometry(infile)  # TYPE_STRUCT
        self.cuttingTriangles = hkBitField(infile)  # TYPE_STRUCT
