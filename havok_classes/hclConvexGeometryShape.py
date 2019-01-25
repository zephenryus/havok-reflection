from .hclShape import hclShape
from .common import any, vector4
from .hkAabb import hkAabb
import struct


class hclConvexGeometryShape(hclShape):
    tetrahedraGrid: any
    gridCells: any
    tetrahedraEquations: any
    localFromWorld: any
    worldFromLocal: any
    objAabb: hkAabb
    geomCentroid: vector4
    invCellSize: vector4
    gridRes: int

    def __init__(self, infile):
        self.tetrahedraGrid = any(infile)  # TYPE_ARRAY
        self.gridCells = any(infile)  # TYPE_ARRAY
        self.tetrahedraEquations = any(infile)  # TYPE_ARRAY
        self.localFromWorld = any(infile)  # TYPE_TRANSFORM
        self.worldFromLocal = any(infile)  # TYPE_TRANSFORM
        self.objAabb = hkAabb(infile)  # TYPE_STRUCT
        self.geomCentroid = struct.unpack('>4f', infile.read(16))
        self.invCellSize = struct.unpack('>4f', infile.read(16))
        self.gridRes = struct.unpack('>H', infile.read(2))
