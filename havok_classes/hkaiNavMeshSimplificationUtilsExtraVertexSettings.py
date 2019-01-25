from enum import Enum
from .enums import VertexSelectionMethod
import struct
from typing import List
from .common import get_array


class VertexSelectionMethod(Enum):
    PROPORTIONAL_TO_AREA = 0
    PROPORTIONAL_TO_VERTICES = 1


class hkaiNavMeshSimplificationUtilsExtraVertexSettings(object):
    vertexSelectionMethod: VertexSelectionMethod
    vertexFraction: float
    areaFraction: float
    minPartitionArea: float
    numSmoothingIterations: int
    iterationDamping: float
    addVerticesOnBoundaryEdges: bool
    addVerticesOnPartitionBorders: bool
    boundaryEdgeSplitLength: float
    partitionBordersSplitLength: float
    userVertexOnBoundaryTolerance: float
    userVertices: List[vector4]

    def __init__(self, infile):
        self.vertexSelectionMethod = VertexSelectionMethod(infile)  # TYPE_ENUM:TYPE_UINT8
        self.vertexFraction = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.areaFraction = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.minPartitionArea = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.numSmoothingIterations = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.iterationDamping = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.addVerticesOnBoundaryEdges = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.addVerticesOnPartitionBorders = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.boundaryEdgeSplitLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.partitionBordersSplitLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.userVertexOnBoundaryTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.userVertices = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4

    def __repr__(self):
        return "<{class_name} vertexSelectionMethod={vertexSelectionMethod}, vertexFraction={vertexFraction}, areaFraction={areaFraction}, minPartitionArea={minPartitionArea}, numSmoothingIterations={numSmoothingIterations}, iterationDamping={iterationDamping}, addVerticesOnBoundaryEdges={addVerticesOnBoundaryEdges}, addVerticesOnPartitionBorders={addVerticesOnPartitionBorders}, boundaryEdgeSplitLength={boundaryEdgeSplitLength}, partitionBordersSplitLength={partitionBordersSplitLength}, userVertexOnBoundaryTolerance={userVertexOnBoundaryTolerance}, userVertices=[{userVertices}]>".format(**{
            "class_name": self.__class__.__name__,
            "vertexSelectionMethod": self.vertexSelectionMethod,
            "vertexFraction": self.vertexFraction,
            "areaFraction": self.areaFraction,
            "minPartitionArea": self.minPartitionArea,
            "numSmoothingIterations": self.numSmoothingIterations,
            "iterationDamping": self.iterationDamping,
            "addVerticesOnBoundaryEdges": self.addVerticesOnBoundaryEdges,
            "addVerticesOnPartitionBorders": self.addVerticesOnPartitionBorders,
            "boundaryEdgeSplitLength": self.boundaryEdgeSplitLength,
            "partitionBordersSplitLength": self.partitionBordersSplitLength,
            "userVertexOnBoundaryTolerance": self.userVertexOnBoundaryTolerance,
            "userVertices": self.userVertices,
        })
