import struct


class hkaQuantizedAnimationTrackCompressionParams(object):
    rotationTolerance: float
    translationTolerance: float
    scaleTolerance: float
    floatingTolerance: float

    def __init__(self, infile):
        self.rotationTolerance = struct.unpack('>f', infile.read(4))
        self.translationTolerance = struct.unpack('>f', infile.read(4))
        self.scaleTolerance = struct.unpack('>f', infile.read(4))
        self.floatingTolerance = struct.unpack('>f', infile.read(4))
