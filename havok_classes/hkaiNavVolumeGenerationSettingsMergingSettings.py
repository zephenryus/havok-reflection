import struct


class hkaiNavVolumeGenerationSettingsMergingSettings(object):
    nodeWeight: float
    edgeWeight: float
    estimateNewEdges: bool
    iterationsStabilizationThreshold: int
    slopeThreshold: float
    maxMergingIterations: int
    randomSeed: int
    multiplier: float
    useSimpleFirstMergePass: bool

    def __init__(self, infile):
        self.nodeWeight = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.edgeWeight = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.estimateNewEdges = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.iterationsStabilizationThreshold = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.slopeThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxMergingIterations = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.randomSeed = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.multiplier = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.useSimpleFirstMergePass = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} nodeWeight={nodeWeight}, edgeWeight={edgeWeight}, estimateNewEdges={estimateNewEdges}, iterationsStabilizationThreshold={iterationsStabilizationThreshold}, slopeThreshold={slopeThreshold}, maxMergingIterations={maxMergingIterations}, randomSeed={randomSeed}, multiplier={multiplier}, useSimpleFirstMergePass={useSimpleFirstMergePass}>".format(**{
            "class_name": self.__class__.__name__,
            "nodeWeight": self.nodeWeight,
            "edgeWeight": self.edgeWeight,
            "estimateNewEdges": self.estimateNewEdges,
            "iterationsStabilizationThreshold": self.iterationsStabilizationThreshold,
            "slopeThreshold": self.slopeThreshold,
            "maxMergingIterations": self.maxMergingIterations,
            "randomSeed": self.randomSeed,
            "multiplier": self.multiplier,
            "useSimpleFirstMergePass": self.useSimpleFirstMergePass,
        })
