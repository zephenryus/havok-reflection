from .hkaiVolume import hkaiVolume
import struct
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

    def __init__(self, infile):
        self.volume = hkaiVolume(infile)  # TYPE_POINTER
        self.material = struct.unpack('>i', infile.read(4))
        self.characterWidthUsage = CharacterWidthUsage(infile)  # TYPE_ENUM
        self.maxWalkableSlope = struct.unpack('>f', infile.read(4))
        self.edgeMatchingParams = hkaiNavMeshEdgeMatchingParameters(infile)  # TYPE_STRUCT
        self.simplificationSettings = hkaiNavMeshSimplificationUtilsSettings(infile)  # TYPE_STRUCT
