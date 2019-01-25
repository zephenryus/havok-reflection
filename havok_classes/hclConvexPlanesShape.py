from .hclShape import hclShape
from typing import List
from .common import get_array
from .hkAabb import hkAabb
import struct


class hclConvexPlanesShape(hclShape):
    planeEquations: List[vector4]
    localFromWorld: any
    worldFromLocal: any
    objAabb: hkAabb
    geomCentroid: vector4

    def __init__(self, infile):
        self.planeEquations = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.localFromWorld = any(infile)  # TYPE_TRANSFORM:TYPE_VOID
        self.worldFromLocal = any(infile)  # TYPE_TRANSFORM:TYPE_VOID
        self.objAabb = hkAabb(infile)  # TYPE_STRUCT:TYPE_VOID
        self.geomCentroid = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} planeEquations=[{planeEquations}], localFromWorld={localFromWorld}, worldFromLocal={worldFromLocal}, objAabb={objAabb}, geomCentroid={geomCentroid}>".format(**{
            "class_name": self.__class__.__name__,
            "planeEquations": self.planeEquations,
            "localFromWorld": self.localFromWorld,
            "worldFromLocal": self.worldFromLocal,
            "objAabb": self.objAabb,
            "geomCentroid": self.geomCentroid,
        })
