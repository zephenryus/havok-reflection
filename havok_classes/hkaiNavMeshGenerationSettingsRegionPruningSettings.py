import struct
from .common import any
from .hkaiNavMeshGenerationSettingsRegionPruningSettingsRegionConnection import hkaiNavMeshGenerationSettingsRegionPruningSettingsRegionConnection


class hkaiNavMeshGenerationSettingsRegionPruningSettings(object):
    minRegionArea: float
    minDistanceToSeedPoints: float
    borderPreservationTolerance: float
    preserveVerticalBorderRegions: bool
    pruneBeforeTriangulation: bool
    regionSeedPoints: any
    regionConnections: hkaiNavMeshGenerationSettingsRegionPruningSettingsRegionConnection

    def __init__(self, infile):
        self.minRegionArea = struct.unpack('>f', infile.read(4))
        self.minDistanceToSeedPoints = struct.unpack('>f', infile.read(4))
        self.borderPreservationTolerance = struct.unpack('>f', infile.read(4))
        self.preserveVerticalBorderRegions = struct.unpack('>?', infile.read(1))
        self.pruneBeforeTriangulation = struct.unpack('>?', infile.read(1))
        self.regionSeedPoints = any(infile)  # TYPE_ARRAY
        self.regionConnections = hkaiNavMeshGenerationSettingsRegionPruningSettingsRegionConnection(infile)  # TYPE_ARRAY
