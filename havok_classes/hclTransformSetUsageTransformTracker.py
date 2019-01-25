from .hkBitField import hkBitField


class hclTransformSetUsageTransformTracker(object):
    read: hkBitField
    readBeforeWrite: hkBitField
    written: hkBitField

    def __init__(self, infile):
        self.read = hkBitField(infile)  # TYPE_STRUCT
        self.readBeforeWrite = hkBitField(infile)  # TYPE_STRUCT
        self.written = hkBitField(infile)  # TYPE_STRUCT
