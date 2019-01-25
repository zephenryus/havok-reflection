import struct


class hkaiNavMeshGenerationSettingsWallClimbingSettings(object):
    enableWallClimbing: bool
    excludeWalkableFaces: bool

    def __init__(self, infile):
        self.enableWallClimbing = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.excludeWalkableFaces = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} enableWallClimbing={enableWallClimbing}, excludeWalkableFaces={excludeWalkableFaces}>".format(**{
            "class_name": self.__class__.__name__,
            "enableWallClimbing": self.enableWallClimbing,
            "excludeWalkableFaces": self.excludeWalkableFaces,
        })
