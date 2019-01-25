from .hkBitField import hkBitField


class hclTransformSetUsageTransformTracker(object):
    read: hkBitField
    readBeforeWrite: hkBitField
    written: hkBitField

    def __init__(self, infile):
        self.read = hkBitField(infile)  # TYPE_STRUCT:TYPE_VOID
        self.readBeforeWrite = hkBitField(infile)  # TYPE_STRUCT:TYPE_VOID
        self.written = hkBitField(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} read={read}, readBeforeWrite={readBeforeWrite}, written={written}>".format(**{
            "class_name": self.__class__.__name__,
            "read": self.read,
            "readBeforeWrite": self.readBeforeWrite,
            "written": self.written,
        })
