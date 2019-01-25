from .hkReferencedObject import hkReferencedObject
from .hkGeometry import hkGeometry
from .hkBitField import hkBitField


class hkaiCuttingGeometryInfo(hkReferencedObject):
    geometry: hkGeometry
    cuttingTriangles: hkBitField

    def __init__(self, infile):
        self.geometry = hkGeometry(infile)  # TYPE_STRUCT:TYPE_VOID
        self.cuttingTriangles = hkBitField(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} geometry={geometry}, cuttingTriangles={cuttingTriangles}>".format(**{
            "class_name": self.__class__.__name__,
            "geometry": self.geometry,
            "cuttingTriangles": self.cuttingTriangles,
        })
