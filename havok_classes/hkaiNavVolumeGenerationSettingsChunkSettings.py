import struct


class hkaiNavVolumeGenerationSettingsChunkSettings(object):
    maxChunkSizeX: int
    maxChunkSizeY: int
    maxChunkSizeZ: int
    doGreedyMergeAfterCombine: bool

    def __init__(self, infile):
        self.maxChunkSizeX = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.maxChunkSizeY = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.maxChunkSizeZ = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.doGreedyMergeAfterCombine = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} maxChunkSizeX={maxChunkSizeX}, maxChunkSizeY={maxChunkSizeY}, maxChunkSizeZ={maxChunkSizeZ}, doGreedyMergeAfterCombine={doGreedyMergeAfterCombine}>".format(**{
            "class_name": self.__class__.__name__,
            "maxChunkSizeX": self.maxChunkSizeX,
            "maxChunkSizeY": self.maxChunkSizeY,
            "maxChunkSizeZ": self.maxChunkSizeZ,
            "doGreedyMergeAfterCombine": self.doGreedyMergeAfterCombine,
        })
