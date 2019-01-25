from .enums import SplitAndGenerateOptions, SplitMethod
import struct
from .common import any


class hkaiSplitGenerationUtilsSettings(object):
    simplificationOptions: SplitAndGenerateOptions
    splitMethod: SplitMethod
    generateClusterGraphs: bool
    desiredFacesPerCluster: int
    costModifier: any
    shelver: any
    borderPreserveShrinkSize: float
    streamingEdgeMatchTolerance: float
    numX: int
    numY: int
    maxSplits: int
    desiredTrisPerChunk: int
    saveInputSnapshot: bool
    snapshotFilename: str

    def __init__(self, infile):
        self.simplificationOptions = SplitAndGenerateOptions(infile)  # TYPE_ENUM
        self.splitMethod = SplitMethod(infile)  # TYPE_ENUM
        self.generateClusterGraphs = struct.unpack('>?', infile.read(1))
        self.desiredFacesPerCluster = struct.unpack('>i', infile.read(4))
        self.costModifier = any(infile)  # TYPE_POINTER
        self.shelver = any(infile)  # TYPE_POINTER
        self.borderPreserveShrinkSize = struct.unpack('>f', infile.read(4))
        self.streamingEdgeMatchTolerance = struct.unpack('>f', infile.read(4))
        self.numX = struct.unpack('>i', infile.read(4))
        self.numY = struct.unpack('>i', infile.read(4))
        self.maxSplits = struct.unpack('>i', infile.read(4))
        self.desiredTrisPerChunk = struct.unpack('>i', infile.read(4))
        self.saveInputSnapshot = struct.unpack('>?', infile.read(1))
        self.snapshotFilename = struct.unpack('>s', infile.read(0))
