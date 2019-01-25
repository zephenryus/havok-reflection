import struct


class hkaiNavVolumeGenerationSettingsChunkSettings(object):
    maxChunkSizeX: int
    maxChunkSizeY: int
    maxChunkSizeZ: int
    doGreedyMergeAfterCombine: bool

    def __init__(self, infile):
        self.maxChunkSizeX = struct.unpack('>H', infile.read(2))
        self.maxChunkSizeY = struct.unpack('>H', infile.read(2))
        self.maxChunkSizeZ = struct.unpack('>H', infile.read(2))
        self.doGreedyMergeAfterCombine = struct.unpack('>?', infile.read(1))
