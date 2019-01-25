from .hkaiVolume import hkaiVolume
import struct
from .enums import CharacterWidthUsage
from .hkaiNavMeshEdgeMatchingParameters import hkaiNavMeshEdgeMatchingParameters
from .hkaiNavMeshSimplificationUtilsSettings import hkaiNavMeshSimplificationUtilsSettings


class hkaiNavMeshGenerationSettingsOverrideSettings(object):
    volume: any
    material: int
    characterWidthUsage: CharacterWidthUsage
    maxWalkableSlope: float
    edgeMatchingParams: hkaiNavMeshEdgeMatchingParameters
    simplificationSettings: hkaiNavMeshSimplificationUtilsSettings

    def __init__(self, infile):
        self.volume = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.material = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.characterWidthUsage = CharacterWidthUsage(infile)  # TYPE_ENUM:TYPE_UINT8
        self.maxWalkableSlope = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.edgeMatchingParams = hkaiNavMeshEdgeMatchingParameters(infile)  # TYPE_STRUCT:TYPE_VOID
        self.simplificationSettings = hkaiNavMeshSimplificationUtilsSettings(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} volume={volume}, material={material}, characterWidthUsage={characterWidthUsage}, maxWalkableSlope={maxWalkableSlope}, edgeMatchingParams={edgeMatchingParams}, simplificationSettings={simplificationSettings}>".format(**{
            "class_name": self.__class__.__name__,
            "volume": self.volume,
            "material": self.material,
            "characterWidthUsage": self.characterWidthUsage,
            "maxWalkableSlope": self.maxWalkableSlope,
            "edgeMatchingParams": self.edgeMatchingParams,
            "simplificationSettings": self.simplificationSettings,
        })
