from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkAabb import hkAabb
import struct
from .enums import CellWidthToResolutionRounding
from .hkaiNavVolumeGenerationSettingsChunkSettings import hkaiNavVolumeGenerationSettingsChunkSettings
from .hkaiNavVolumeGenerationSettingsMergingSettings import hkaiNavVolumeGenerationSettingsMergingSettings
from typing import List
from .common import get_array
from .hkaiNavVolumeGenerationSettingsMaterialConstructionInfo import hkaiNavVolumeGenerationSettingsMaterialConstructionInfo
from .hkaiCarver import hkaiCarver
from .hkaiMaterialPainter import hkaiMaterialPainter


class MaterialFlagsBits(Enum):
    MATERIAL_NONE = 0
    MATERIAL_BLOCKING = 1
    MATERIAL_DEFAULT = 1


class CellWidthToResolutionRounding(Enum):
    ROUND_TO_ZERO = 0
    ROUND_TO_NEAREST = 1


class hkaiNavVolumeGenerationSettings(hkReferencedObject):
    volumeAabb: hkAabb
    maxHorizontalRange: float
    maxVerticalRange: float
    up: vector4
    characterHeight: float
    characterDepth: float
    characterWidth: float
    cellWidth: float
    resolutionRoundingMode: CellWidthToResolutionRounding
    chunkSettings: hkaiNavVolumeGenerationSettingsChunkSettings
    chunkDomainCallback: any
    border: float
    useBorderCells: bool
    mergingSettings: hkaiNavVolumeGenerationSettingsMergingSettings
    minRegionVolume: float
    minDistanceToSeedPoints: float
    regionSeedPoints: List[vector4]
    defaultConstructionInfo: hkaiNavVolumeGenerationSettingsMaterialConstructionInfo
    materialMap: List[hkaiNavVolumeGenerationSettingsMaterialConstructionInfo]
    carvers: List[hkaiCarver]
    painters: List[hkaiMaterialPainter]
    saveInputSnapshot: bool
    snapshotFilename: str

    def __init__(self, infile):
        self.volumeAabb = hkAabb(infile)  # TYPE_STRUCT:TYPE_VOID
        self.maxHorizontalRange = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxVerticalRange = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.up = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.characterHeight = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.characterDepth = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.characterWidth = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.cellWidth = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.resolutionRoundingMode = CellWidthToResolutionRounding(infile)  # TYPE_ENUM:TYPE_UINT8
        self.chunkSettings = hkaiNavVolumeGenerationSettingsChunkSettings(infile)  # TYPE_STRUCT:TYPE_VOID
        self.chunkDomainCallback = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.border = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.useBorderCells = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.mergingSettings = hkaiNavVolumeGenerationSettingsMergingSettings(infile)  # TYPE_STRUCT:TYPE_VOID
        self.minRegionVolume = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.minDistanceToSeedPoints = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.regionSeedPoints = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.defaultConstructionInfo = hkaiNavVolumeGenerationSettingsMaterialConstructionInfo(infile)  # TYPE_STRUCT:TYPE_VOID
        self.materialMap = get_array(infile, hkaiNavVolumeGenerationSettingsMaterialConstructionInfo, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.carvers = get_array(infile, hkaiCarver, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.painters = get_array(infile, hkaiMaterialPainter, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.saveInputSnapshot = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.snapshotFilename = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} volumeAabb={volumeAabb}, maxHorizontalRange={maxHorizontalRange}, maxVerticalRange={maxVerticalRange}, up={up}, characterHeight={characterHeight}, characterDepth={characterDepth}, characterWidth={characterWidth}, cellWidth={cellWidth}, resolutionRoundingMode={resolutionRoundingMode}, chunkSettings={chunkSettings}, chunkDomainCallback={chunkDomainCallback}, border={border}, useBorderCells={useBorderCells}, mergingSettings={mergingSettings}, minRegionVolume={minRegionVolume}, minDistanceToSeedPoints={minDistanceToSeedPoints}, regionSeedPoints=[{regionSeedPoints}], defaultConstructionInfo={defaultConstructionInfo}, materialMap=[{materialMap}], carvers=[{carvers}], painters=[{painters}], saveInputSnapshot={saveInputSnapshot}, snapshotFilename=\"{snapshotFilename}\">".format(**{
            "class_name": self.__class__.__name__,
            "volumeAabb": self.volumeAabb,
            "maxHorizontalRange": self.maxHorizontalRange,
            "maxVerticalRange": self.maxVerticalRange,
            "up": self.up,
            "characterHeight": self.characterHeight,
            "characterDepth": self.characterDepth,
            "characterWidth": self.characterWidth,
            "cellWidth": self.cellWidth,
            "resolutionRoundingMode": self.resolutionRoundingMode,
            "chunkSettings": self.chunkSettings,
            "chunkDomainCallback": self.chunkDomainCallback,
            "border": self.border,
            "useBorderCells": self.useBorderCells,
            "mergingSettings": self.mergingSettings,
            "minRegionVolume": self.minRegionVolume,
            "minDistanceToSeedPoints": self.minDistanceToSeedPoints,
            "regionSeedPoints": self.regionSeedPoints,
            "defaultConstructionInfo": self.defaultConstructionInfo,
            "materialMap": self.materialMap,
            "carvers": self.carvers,
            "painters": self.painters,
            "saveInputSnapshot": self.saveInputSnapshot,
            "snapshotFilename": self.snapshotFilename,
        })
