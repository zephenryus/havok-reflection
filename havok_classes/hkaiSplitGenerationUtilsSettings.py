from .enums import SplitAndGenerateOptions, SplitMethod
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
