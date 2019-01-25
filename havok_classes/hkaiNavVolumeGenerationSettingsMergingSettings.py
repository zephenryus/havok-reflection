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
        self.nodeWeight = struct.unpack('>f', infile.read(4))
        self.edgeWeight = struct.unpack('>f', infile.read(4))
        self.estimateNewEdges = struct.unpack('>?', infile.read(1))
        self.iterationsStabilizationThreshold = struct.unpack('>i', infile.read(4))
        self.slopeThreshold = struct.unpack('>f', infile.read(4))
        self.maxMergingIterations = struct.unpack('>i', infile.read(4))
        self.randomSeed = struct.unpack('>i', infile.read(4))
        self.multiplier = struct.unpack('>f', infile.read(4))
        self.useSimpleFirstMergePass = struct.unpack('>?', infile.read(1))
