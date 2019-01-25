import struct
from typing import List
from .common import get_array
from .hkaiNavMeshGenerationSettingsRegionPruningSettingsRegionConnection import hkaiNavMeshGenerationSettingsRegionPruningSettingsRegionConnection


class hkaiNavMeshGenerationSettingsRegionPruningSettings(object):
    minRegionArea: float
    minDistanceToSeedPoints: float
    borderPreservationTolerance: float
    preserveVerticalBorderRegions: bool
    pruneBeforeTriangulation: bool
    regionSeedPoints: List[vector4]
    regionConnections: List[hkaiNavMeshGenerationSettingsRegionPruningSettingsRegionConnection]

    def __init__(self, infile):
        self.minRegionArea = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.minDistanceToSeedPoints = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.borderPreservationTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.preserveVerticalBorderRegions = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.pruneBeforeTriangulation = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.regionSeedPoints = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.regionConnections = get_array(infile, hkaiNavMeshGenerationSettingsRegionPruningSettingsRegionConnection, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} minRegionArea={minRegionArea}, minDistanceToSeedPoints={minDistanceToSeedPoints}, borderPreservationTolerance={borderPreservationTolerance}, preserveVerticalBorderRegions={preserveVerticalBorderRegions}, pruneBeforeTriangulation={pruneBeforeTriangulation}, regionSeedPoints=[{regionSeedPoints}], regionConnections=[{regionConnections}]>".format(**{
            "class_name": self.__class__.__name__,
            "minRegionArea": self.minRegionArea,
            "minDistanceToSeedPoints": self.minDistanceToSeedPoints,
            "borderPreservationTolerance": self.borderPreservationTolerance,
            "preserveVerticalBorderRegions": self.preserveVerticalBorderRegions,
            "pruneBeforeTriangulation": self.pruneBeforeTriangulation,
            "regionSeedPoints": self.regionSeedPoints,
            "regionConnections": self.regionConnections,
        })
