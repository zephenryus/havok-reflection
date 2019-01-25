from .hkReferencedObject import hkReferencedObject
from enum import Enum
import struct
from .common import vector4, any
from .enums import TriangleWinding, EdgeMatchingMetric, CharacterWidthUsage
from .hkaiNavMeshEdgeMatchingParameters import hkaiNavMeshEdgeMatchingParameters
from .hkaiNavMeshGenerationSettingsRegionPruningSettings import hkaiNavMeshGenerationSettingsRegionPruningSettings
from .hkaiNavMeshGenerationSettingsWallClimbingSettings import hkaiNavMeshGenerationSettingsWallClimbingSettings
from .hkAabb import hkAabb
from .hkaiCarver import hkaiCarver
from .hkaiMaterialPainter import hkaiMaterialPainter
from .hkaiNavMeshGenerationSettingsMaterialConstructionPair import hkaiNavMeshGenerationSettingsMaterialConstructionPair
from .hkaiOverlappingTrianglesSettings import hkaiOverlappingTrianglesSettings
from .hkaiNavMeshSimplificationUtilsSettings import hkaiNavMeshSimplificationUtilsSettings
from .hkaiNavMeshGenerationSettingsOverrideSettings import hkaiNavMeshGenerationSettingsOverrideSettings


class ConstructionFlagsBits(Enum):
    MATERIAL_WALKABLE = 1
    MATERIAL_CUTTING = 2
    MATERIAL_WALKABLE_AND_CUTTING = 3


class CharacterWidthUsage(Enum):
    NONE = 0
    BLOCK_EDGES = 1
    SHRINK_NAV_MESH = 2


class TriangleWinding(Enum):
    WINDING_CCW = 0
    WINDING_CW = 1


class EdgeMatchingMetric(Enum):
    ORDER_BY_OVERLAP = 1
    ORDER_BY_DISTANCE = 2


class hkaiNavMeshGenerationSettings(hkReferencedObject):
    characterHeight: float
    up: vector4
    quantizationGridSize: float
    maxWalkableSlope: float
    triangleWinding: TriangleWinding
    degenerateAreaThreshold: float
    degenerateWidthThreshold: float
    convexThreshold: float
    maxNumEdgesPerFace: int
    edgeMatchingParams: hkaiNavMeshEdgeMatchingParameters
    edgeMatchingMetric: EdgeMatchingMetric
    edgeConnectionIterations: int
    regionPruningSettings: hkaiNavMeshGenerationSettingsRegionPruningSettings
    wallClimbingSettings: hkaiNavMeshGenerationSettingsWallClimbingSettings
    boundsAabb: hkAabb
    carvers: hkaiCarver
    painters: hkaiMaterialPainter
    painterOverlapCallback: any
    defaultConstructionProperties: any
    materialMap: hkaiNavMeshGenerationSettingsMaterialConstructionPair
    fixupOverlappingTriangles: bool
    overlappingTrianglesSettings: hkaiOverlappingTrianglesSettings
    weldInputVertices: bool
    weldThreshold: float
    minCharacterWidth: float
    characterWidthUsage: CharacterWidthUsage
    enableSimplification: bool
    simplificationSettings: hkaiNavMeshSimplificationUtilsSettings
    carvedMaterialDeprecated: int
    carvedCuttingMaterialDeprecated: int
    checkEdgeGeometryConsistency: bool
    saveInputSnapshot: bool
    snapshotFilename: str
    overrideSettings: hkaiNavMeshGenerationSettingsOverrideSettings

    def __init__(self, infile):
        self.characterHeight = struct.unpack('>f', infile.read(4))
        self.up = struct.unpack('>4f', infile.read(16))
        self.quantizationGridSize = struct.unpack('>f', infile.read(4))
        self.maxWalkableSlope = struct.unpack('>f', infile.read(4))
        self.triangleWinding = TriangleWinding(infile)  # TYPE_ENUM
        self.degenerateAreaThreshold = struct.unpack('>f', infile.read(4))
        self.degenerateWidthThreshold = struct.unpack('>f', infile.read(4))
        self.convexThreshold = struct.unpack('>f', infile.read(4))
        self.maxNumEdgesPerFace = struct.unpack('>i', infile.read(4))
        self.edgeMatchingParams = hkaiNavMeshEdgeMatchingParameters(infile)  # TYPE_STRUCT
        self.edgeMatchingMetric = EdgeMatchingMetric(infile)  # TYPE_ENUM
        self.edgeConnectionIterations = struct.unpack('>i', infile.read(4))
        self.regionPruningSettings = hkaiNavMeshGenerationSettingsRegionPruningSettings(infile)  # TYPE_STRUCT
        self.wallClimbingSettings = hkaiNavMeshGenerationSettingsWallClimbingSettings(infile)  # TYPE_STRUCT
        self.boundsAabb = hkAabb(infile)  # TYPE_STRUCT
        self.carvers = hkaiCarver(infile)  # TYPE_ARRAY
        self.painters = hkaiMaterialPainter(infile)  # TYPE_ARRAY
        self.painterOverlapCallback = any(infile)  # TYPE_POINTER
        self.defaultConstructionProperties = any(infile)  # TYPE_FLAGS
        self.materialMap = hkaiNavMeshGenerationSettingsMaterialConstructionPair(infile)  # TYPE_ARRAY
        self.fixupOverlappingTriangles = struct.unpack('>?', infile.read(1))
        self.overlappingTrianglesSettings = hkaiOverlappingTrianglesSettings(infile)  # TYPE_STRUCT
        self.weldInputVertices = struct.unpack('>?', infile.read(1))
        self.weldThreshold = struct.unpack('>f', infile.read(4))
        self.minCharacterWidth = struct.unpack('>f', infile.read(4))
        self.characterWidthUsage = CharacterWidthUsage(infile)  # TYPE_ENUM
        self.enableSimplification = struct.unpack('>?', infile.read(1))
        self.simplificationSettings = hkaiNavMeshSimplificationUtilsSettings(infile)  # TYPE_STRUCT
        self.carvedMaterialDeprecated = struct.unpack('>i', infile.read(4))
        self.carvedCuttingMaterialDeprecated = struct.unpack('>i', infile.read(4))
        self.checkEdgeGeometryConsistency = struct.unpack('>?', infile.read(1))
        self.saveInputSnapshot = struct.unpack('>?', infile.read(1))
        self.snapshotFilename = struct.unpack('>s', infile.read(0))
        self.overrideSettings = hkaiNavMeshGenerationSettingsOverrideSettings(infile)  # TYPE_ARRAY
