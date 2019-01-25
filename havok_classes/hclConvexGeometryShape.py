from .hclShape import hclShape
from typing import List
from .common import get_array
from .hkAabb import hkAabb
import struct


class hclConvexGeometryShape(hclShape):
    tetrahedraGrid: List[int]
    gridCells: List[int]
    tetrahedraEquations: List[any]
    localFromWorld: any
    worldFromLocal: any
    objAabb: hkAabb
    geomCentroid: vector4
    invCellSize: vector4
    gridRes: int

    def __init__(self, infile):
        self.tetrahedraGrid = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.gridCells = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.tetrahedraEquations = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_MATRIX4
        self.localFromWorld = any(infile)  # TYPE_TRANSFORM:TYPE_VOID
        self.worldFromLocal = any(infile)  # TYPE_TRANSFORM:TYPE_VOID
        self.objAabb = hkAabb(infile)  # TYPE_STRUCT:TYPE_VOID
        self.geomCentroid = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.invCellSize = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.gridRes = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} tetrahedraGrid=[{tetrahedraGrid}], gridCells=[{gridCells}], tetrahedraEquations=[{tetrahedraEquations}], localFromWorld={localFromWorld}, worldFromLocal={worldFromLocal}, objAabb={objAabb}, geomCentroid={geomCentroid}, invCellSize={invCellSize}, gridRes={gridRes}>".format(**{
            "class_name": self.__class__.__name__,
            "tetrahedraGrid": self.tetrahedraGrid,
            "gridCells": self.gridCells,
            "tetrahedraEquations": self.tetrahedraEquations,
            "localFromWorld": self.localFromWorld,
            "worldFromLocal": self.worldFromLocal,
            "objAabb": self.objAabb,
            "geomCentroid": self.geomCentroid,
            "invCellSize": self.invCellSize,
            "gridRes": self.gridRes,
        })
