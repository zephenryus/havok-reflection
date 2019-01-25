from .hkpShape import hkpShape
import struct
from .hkpCdBody import hkpCdBody


class hkpCdBody(object):
    shape: any
    shapeKey: int
    motion: any
    parent: any

    def __init__(self, infile):
        self.shape = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.shapeKey = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.motion = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.parent = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} shape={shape}, shapeKey={shapeKey}, motion={motion}, parent={parent}>".format(**{
            "class_name": self.__class__.__name__,
            "shape": self.shape,
            "shapeKey": self.shapeKey,
            "motion": self.motion,
            "parent": self.parent,
        })
