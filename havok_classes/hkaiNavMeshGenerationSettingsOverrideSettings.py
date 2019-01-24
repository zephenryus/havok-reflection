from .hkaiVolume import hkaiVolume
from .enums import CharacterWidthUsage
from .hkaiNavMeshEdgeMatchingParameters import hkaiNavMeshEdgeMatchingParameters
from .hkaiNavMeshSimplificationUtilsSettings import hkaiNavMeshSimplificationUtilsSettings


class hkaiNavMeshGenerationSettingsOverrideSettings(object):
    volume: hkaiVolume
    material: int
    characterWidthUsage: CharacterWidthUsage
    maxWalkableSlope: float
    edgeMatchingParams: hkaiNavMeshEdgeMatchingParameters
    simplificationSettings: hkaiNavMeshSimplificationUtilsSettings
