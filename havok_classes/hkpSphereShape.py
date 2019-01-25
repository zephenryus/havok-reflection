from .hkpConvexShape import hkpConvexShape
import struct


class hkpSphereShape(hkpConvexShape):
    pad16: int

    def __init__(self, infile):
        self.pad16 = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} pad16={pad16}>".format(**{
            "class_name": self.__class__.__name__,
            "pad16": self.pad16,
        })
