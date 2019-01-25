from .enums import SplitAndGenerateOptions, SplitMethod
import struct


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
        self.simplificationOptions = SplitAndGenerateOptions(infile)  # TYPE_ENUM:TYPE_UINT8
        self.splitMethod = SplitMethod(infile)  # TYPE_ENUM:TYPE_UINT8
        self.generateClusterGraphs = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.desiredFacesPerCluster = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.costModifier = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.shelver = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.borderPreserveShrinkSize = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.streamingEdgeMatchTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.numX = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numY = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.maxSplits = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.desiredTrisPerChunk = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.saveInputSnapshot = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.snapshotFilename = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} simplificationOptions={simplificationOptions}, splitMethod={splitMethod}, generateClusterGraphs={generateClusterGraphs}, desiredFacesPerCluster={desiredFacesPerCluster}, costModifier={costModifier}, shelver={shelver}, borderPreserveShrinkSize={borderPreserveShrinkSize}, streamingEdgeMatchTolerance={streamingEdgeMatchTolerance}, numX={numX}, numY={numY}, maxSplits={maxSplits}, desiredTrisPerChunk={desiredTrisPerChunk}, saveInputSnapshot={saveInputSnapshot}, snapshotFilename=\"{snapshotFilename}\">".format(**{
            "class_name": self.__class__.__name__,
            "simplificationOptions": self.simplificationOptions,
            "splitMethod": self.splitMethod,
            "generateClusterGraphs": self.generateClusterGraphs,
            "desiredFacesPerCluster": self.desiredFacesPerCluster,
            "costModifier": self.costModifier,
            "shelver": self.shelver,
            "borderPreserveShrinkSize": self.borderPreserveShrinkSize,
            "streamingEdgeMatchTolerance": self.streamingEdgeMatchTolerance,
            "numX": self.numX,
            "numY": self.numY,
            "maxSplits": self.maxSplits,
            "desiredTrisPerChunk": self.desiredTrisPerChunk,
            "saveInputSnapshot": self.saveInputSnapshot,
            "snapshotFilename": self.snapshotFilename,
        })
