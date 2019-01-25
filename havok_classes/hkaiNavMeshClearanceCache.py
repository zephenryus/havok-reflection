from .hkReferencedObject import hkReferencedObject
import struct
from .common import any
from .hkaiNavMeshClearanceCacheMcpDataInteger import hkaiNavMeshClearanceCacheMcpDataInteger


class hkaiNavMeshClearanceCache(hkReferencedObject):
    clearanceCeiling: float
    clearanceIntToRealMultiplier: float
    clearanceRealToIntMultiplier: float
    faceOffsets: any
    edgePairClearances: any
    unusedEdgePairElements: int
    mcpData: hkaiNavMeshClearanceCacheMcpDataInteger
    vertexClearances: any

    def __init__(self, infile):
        self.clearanceCeiling = struct.unpack('>f', infile.read(4))
        self.clearanceIntToRealMultiplier = struct.unpack('>f', infile.read(4))
        self.clearanceRealToIntMultiplier = struct.unpack('>f', infile.read(4))
        self.faceOffsets = any(infile)  # TYPE_ARRAY
        self.edgePairClearances = any(infile)  # TYPE_ARRAY
        self.unusedEdgePairElements = struct.unpack('>i', infile.read(4))
        self.mcpData = hkaiNavMeshClearanceCacheMcpDataInteger(infile)  # TYPE_ARRAY
        self.vertexClearances = any(infile)  # TYPE_ARRAY
