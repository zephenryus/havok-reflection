from .hkReferencedObject import hkReferencedObject
from enum import Enum
import struct
from .enums import TriangleWinding, EdgeMatchingMetric, CharacterWidthUsage
from .hkaiNavMeshEdgeMatchingParameters import hkaiNavMeshEdgeMatchingParameters
from .hkaiNavMeshGenerationSettingsRegionPruningSettings import hkaiNavMeshGenerationSettingsRegionPruningSettings
from .hkaiNavMeshGenerationSettingsWallClimbingSettings import hkaiNavMeshGenerationSettingsWallClimbingSettings
from .hkAabb import hkAabb
from typing import List
from .common import get_array
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
    carvers: List[hkaiCarver]
    painters: List[hkaiMaterialPainter]
    painterOverlapCallback: any
    defaultConstructionProperties: any
    materialMap: List[hkaiNavMeshGenerationSettingsMaterialConstructionPair]
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
    overrideSettings: List[hkaiNavMeshGenerationSettingsOverrideSettings]

    def __init__(self, infile):
        self.characterHeight = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.up = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.quantizationGridSize = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxWalkableSlope = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.triangleWinding = TriangleWinding(infile)  # TYPE_ENUM:TYPE_UINT8
        self.degenerateAreaThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.degenerateWidthThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.convexThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxNumEdgesPerFace = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.edgeMatchingParams = hkaiNavMeshEdgeMatchingParameters(infile)  # TYPE_STRUCT:TYPE_VOID
        self.edgeMatchingMetric = EdgeMatchingMetric(infile)  # TYPE_ENUM:TYPE_UINT32
        self.edgeConnectionIterations = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.regionPruningSettings = hkaiNavMeshGenerationSettingsRegionPruningSettings(infile)  # TYPE_STRUCT:TYPE_VOID
        self.wallClimbingSettings = hkaiNavMeshGenerationSettingsWallClimbingSettings(infile)  # TYPE_STRUCT:TYPE_VOID
        self.boundsAabb = hkAabb(infile)  # TYPE_STRUCT:TYPE_VOID
        self.carvers = get_array(infile, hkaiCarver, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.painters = get_array(infile, hkaiMaterialPainter, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.painterOverlapCallback = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.defaultConstructionProperties = any(infile)  # TYPE_FLAGS:TYPE_UINT32
        self.materialMap = get_array(infile, hkaiNavMeshGenerationSettingsMaterialConstructionPair, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.fixupOverlappingTriangles = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.overlappingTrianglesSettings = hkaiOverlappingTrianglesSettings(infile)  # TYPE_STRUCT:TYPE_VOID
        self.weldInputVertices = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.weldThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.minCharacterWidth = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.characterWidthUsage = CharacterWidthUsage(infile)  # TYPE_ENUM:TYPE_UINT8
        self.enableSimplification = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.simplificationSettings = hkaiNavMeshSimplificationUtilsSettings(infile)  # TYPE_STRUCT:TYPE_VOID
        self.carvedMaterialDeprecated = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.carvedCuttingMaterialDeprecated = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.checkEdgeGeometryConsistency = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.saveInputSnapshot = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.snapshotFilename = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.overrideSettings = get_array(infile, hkaiNavMeshGenerationSettingsOverrideSettings, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} characterHeight={characterHeight}, up={up}, quantizationGridSize={quantizationGridSize}, maxWalkableSlope={maxWalkableSlope}, triangleWinding={triangleWinding}, degenerateAreaThreshold={degenerateAreaThreshold}, degenerateWidthThreshold={degenerateWidthThreshold}, convexThreshold={convexThreshold}, maxNumEdgesPerFace={maxNumEdgesPerFace}, edgeMatchingParams={edgeMatchingParams}, edgeMatchingMetric={edgeMatchingMetric}, edgeConnectionIterations={edgeConnectionIterations}, regionPruningSettings={regionPruningSettings}, wallClimbingSettings={wallClimbingSettings}, boundsAabb={boundsAabb}, carvers=[{carvers}], painters=[{painters}], painterOverlapCallback={painterOverlapCallback}, defaultConstructionProperties={defaultConstructionProperties}, materialMap=[{materialMap}], fixupOverlappingTriangles={fixupOverlappingTriangles}, overlappingTrianglesSettings={overlappingTrianglesSettings}, weldInputVertices={weldInputVertices}, weldThreshold={weldThreshold}, minCharacterWidth={minCharacterWidth}, characterWidthUsage={characterWidthUsage}, enableSimplification={enableSimplification}, simplificationSettings={simplificationSettings}, carvedMaterialDeprecated={carvedMaterialDeprecated}, carvedCuttingMaterialDeprecated={carvedCuttingMaterialDeprecated}, checkEdgeGeometryConsistency={checkEdgeGeometryConsistency}, saveInputSnapshot={saveInputSnapshot}, snapshotFilename=\"{snapshotFilename}\", overrideSettings=[{overrideSettings}]>".format(**{
            "class_name": self.__class__.__name__,
            "characterHeight": self.characterHeight,
            "up": self.up,
            "quantizationGridSize": self.quantizationGridSize,
            "maxWalkableSlope": self.maxWalkableSlope,
            "triangleWinding": self.triangleWinding,
            "degenerateAreaThreshold": self.degenerateAreaThreshold,
            "degenerateWidthThreshold": self.degenerateWidthThreshold,
            "convexThreshold": self.convexThreshold,
            "maxNumEdgesPerFace": self.maxNumEdgesPerFace,
            "edgeMatchingParams": self.edgeMatchingParams,
            "edgeMatchingMetric": self.edgeMatchingMetric,
            "edgeConnectionIterations": self.edgeConnectionIterations,
            "regionPruningSettings": self.regionPruningSettings,
            "wallClimbingSettings": self.wallClimbingSettings,
            "boundsAabb": self.boundsAabb,
            "carvers": self.carvers,
            "painters": self.painters,
            "painterOverlapCallback": self.painterOverlapCallback,
            "defaultConstructionProperties": self.defaultConstructionProperties,
            "materialMap": self.materialMap,
            "fixupOverlappingTriangles": self.fixupOverlappingTriangles,
            "overlappingTrianglesSettings": self.overlappingTrianglesSettings,
            "weldInputVertices": self.weldInputVertices,
            "weldThreshold": self.weldThreshold,
            "minCharacterWidth": self.minCharacterWidth,
            "characterWidthUsage": self.characterWidthUsage,
            "enableSimplification": self.enableSimplification,
            "simplificationSettings": self.simplificationSettings,
            "carvedMaterialDeprecated": self.carvedMaterialDeprecated,
            "carvedCuttingMaterialDeprecated": self.carvedCuttingMaterialDeprecated,
            "checkEdgeGeometryConsistency": self.checkEdgeGeometryConsistency,
            "saveInputSnapshot": self.saveInputSnapshot,
            "snapshotFilename": self.snapshotFilename,
            "overrideSettings": self.overrideSettings,
        })
