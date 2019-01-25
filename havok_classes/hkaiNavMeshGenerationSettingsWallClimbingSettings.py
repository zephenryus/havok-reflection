import struct


class hkaiNavMeshGenerationSettingsWallClimbingSettings(object):
    enableWallClimbing: bool
    excludeWalkableFaces: bool

    def __init__(self, infile):
        self.enableWallClimbing = struct.unpack('>?', infile.read(1))
        self.excludeWalkableFaces = struct.unpack('>?', infile.read(1))
