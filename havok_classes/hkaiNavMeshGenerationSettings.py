from .hkReferencedObject import hkReferencedObject
from enum import Enum
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
