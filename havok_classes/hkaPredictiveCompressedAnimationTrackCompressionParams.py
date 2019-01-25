import struct


class hkaPredictiveCompressedAnimationTrackCompressionParams(object):
    staticTranslationTolerance: float
    staticRotationTolerance: float
    staticScaleTolerance: float
    staticFloatTolerance: float
    dynamicTranslationTolerance: float
    dynamicRotationTolerance: float
    dynamicScaleTolerance: float
    dynamicFloatTolerance: float

    def __init__(self, infile):
        self.staticTranslationTolerance = struct.unpack('>f', infile.read(4))
        self.staticRotationTolerance = struct.unpack('>f', infile.read(4))
        self.staticScaleTolerance = struct.unpack('>f', infile.read(4))
        self.staticFloatTolerance = struct.unpack('>f', infile.read(4))
        self.dynamicTranslationTolerance = struct.unpack('>f', infile.read(4))
        self.dynamicRotationTolerance = struct.unpack('>f', infile.read(4))
        self.dynamicScaleTolerance = struct.unpack('>f', infile.read(4))
        self.dynamicFloatTolerance = struct.unpack('>f', infile.read(4))
