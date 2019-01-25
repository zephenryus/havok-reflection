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
        self.staticTranslationTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.staticRotationTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.staticScaleTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.staticFloatTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.dynamicTranslationTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.dynamicRotationTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.dynamicScaleTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.dynamicFloatTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} staticTranslationTolerance={staticTranslationTolerance}, staticRotationTolerance={staticRotationTolerance}, staticScaleTolerance={staticScaleTolerance}, staticFloatTolerance={staticFloatTolerance}, dynamicTranslationTolerance={dynamicTranslationTolerance}, dynamicRotationTolerance={dynamicRotationTolerance}, dynamicScaleTolerance={dynamicScaleTolerance}, dynamicFloatTolerance={dynamicFloatTolerance}>".format(**{
            "class_name": self.__class__.__name__,
            "staticTranslationTolerance": self.staticTranslationTolerance,
            "staticRotationTolerance": self.staticRotationTolerance,
            "staticScaleTolerance": self.staticScaleTolerance,
            "staticFloatTolerance": self.staticFloatTolerance,
            "dynamicTranslationTolerance": self.dynamicTranslationTolerance,
            "dynamicRotationTolerance": self.dynamicRotationTolerance,
            "dynamicScaleTolerance": self.dynamicScaleTolerance,
            "dynamicFloatTolerance": self.dynamicFloatTolerance,
        })
