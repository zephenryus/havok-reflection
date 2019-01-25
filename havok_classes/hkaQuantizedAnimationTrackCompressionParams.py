import struct


class hkaQuantizedAnimationTrackCompressionParams(object):
    rotationTolerance: float
    translationTolerance: float
    scaleTolerance: float
    floatingTolerance: float

    def __init__(self, infile):
        self.rotationTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.translationTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.scaleTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.floatingTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} rotationTolerance={rotationTolerance}, translationTolerance={translationTolerance}, scaleTolerance={scaleTolerance}, floatingTolerance={floatingTolerance}>".format(**{
            "class_name": self.__class__.__name__,
            "rotationTolerance": self.rotationTolerance,
            "translationTolerance": self.translationTolerance,
            "scaleTolerance": self.scaleTolerance,
            "floatingTolerance": self.floatingTolerance,
        })
