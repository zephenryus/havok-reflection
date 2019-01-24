from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkAabb import hkAabb
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
