from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkAabb import hkAabb
import struct
from .common import vector4, any
from .enums import CellWidthToResolutionRounding
from .hkaiNavVolumeGenerationSettingsChunkSettings import hkaiNavVolumeGenerationSettingsChunkSettings
from .hkaiNavVolumeGenerationSettingsMergingSettings import hkaiNavVolumeGenerationSettingsMergingSettings
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
    regionSeedPoints: any
    defaultConstructionInfo: hkaiNavVolumeGenerationSettingsMaterialConstructionInfo
    materialMap: hkaiNavVolumeGenerationSettingsMaterialConstructionInfo
    carvers: hkaiCarver
    painters: hkaiMaterialPainter
    saveInputSnapshot: bool
    snapshotFilename: str

    def __init__(self, infile):
        self.volumeAabb = hkAabb(infile)  # TYPE_STRUCT
        self.maxHorizontalRange = struct.unpack('>f', infile.read(4))
        self.maxVerticalRange = struct.unpack('>f', infile.read(4))
        self.up = struct.unpack('>4f', infile.read(16))
        self.characterHeight = struct.unpack('>f', infile.read(4))
        self.characterDepth = struct.unpack('>f', infile.read(4))
        self.characterWidth = struct.unpack('>f', infile.read(4))
        self.cellWidth = struct.unpack('>f', infile.read(4))
        self.resolutionRoundingMode = CellWidthToResolutionRounding(infile)  # TYPE_ENUM
        self.chunkSettings = hkaiNavVolumeGenerationSettingsChunkSettings(infile)  # TYPE_STRUCT
        self.chunkDomainCallback = any(infile)  # TYPE_POINTER
        self.border = struct.unpack('>f', infile.read(4))
        self.useBorderCells = struct.unpack('>?', infile.read(1))
        self.mergingSettings = hkaiNavVolumeGenerationSettingsMergingSettings(infile)  # TYPE_STRUCT
        self.minRegionVolume = struct.unpack('>f', infile.read(4))
        self.minDistanceToSeedPoints = struct.unpack('>f', infile.read(4))
        self.regionSeedPoints = any(infile)  # TYPE_ARRAY
        self.defaultConstructionInfo = hkaiNavVolumeGenerationSettingsMaterialConstructionInfo(infile)  # TYPE_STRUCT
        self.materialMap = hkaiNavVolumeGenerationSettingsMaterialConstructionInfo(infile)  # TYPE_ARRAY
        self.carvers = hkaiCarver(infile)  # TYPE_ARRAY
        self.painters = hkaiMaterialPainter(infile)  # TYPE_ARRAY
        self.saveInputSnapshot = struct.unpack('>?', infile.read(1))
        self.snapshotFilename = struct.unpack('>s', infile.read(0))
