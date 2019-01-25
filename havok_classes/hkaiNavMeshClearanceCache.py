from .hkReferencedObject import hkReferencedObject
import struct
from typing import List
from .common import get_array
from .hkaiNavMeshClearanceCacheMcpDataInteger import hkaiNavMeshClearanceCacheMcpDataInteger


class hkaiNavMeshClearanceCache(hkReferencedObject):
    clearanceCeiling: float
    clearanceIntToRealMultiplier: float
    clearanceRealToIntMultiplier: float
    faceOffsets: List[int]
    edgePairClearances: List[int]
    unusedEdgePairElements: int
    mcpData: List[hkaiNavMeshClearanceCacheMcpDataInteger]
    vertexClearances: List[int]

    def __init__(self, infile):
        self.clearanceCeiling = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.clearanceIntToRealMultiplier = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.clearanceRealToIntMultiplier = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.faceOffsets = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.edgePairClearances = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.unusedEdgePairElements = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.mcpData = get_array(infile, hkaiNavMeshClearanceCacheMcpDataInteger, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.vertexClearances = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} clearanceCeiling={clearanceCeiling}, clearanceIntToRealMultiplier={clearanceIntToRealMultiplier}, clearanceRealToIntMultiplier={clearanceRealToIntMultiplier}, faceOffsets=[{faceOffsets}], edgePairClearances=[{edgePairClearances}], unusedEdgePairElements={unusedEdgePairElements}, mcpData=[{mcpData}], vertexClearances=[{vertexClearances}]>".format(**{
            "class_name": self.__class__.__name__,
            "clearanceCeiling": self.clearanceCeiling,
            "clearanceIntToRealMultiplier": self.clearanceIntToRealMultiplier,
            "clearanceRealToIntMultiplier": self.clearanceRealToIntMultiplier,
            "faceOffsets": self.faceOffsets,
            "edgePairClearances": self.edgePairClearances,
            "unusedEdgePairElements": self.unusedEdgePairElements,
            "mcpData": self.mcpData,
            "vertexClearances": self.vertexClearances,
        })
