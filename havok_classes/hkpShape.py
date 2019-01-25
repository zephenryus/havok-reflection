from .hkpShapeBase import hkpShapeBase
import struct


class hkpShape(hkpShapeBase):
    userData: int

    def __init__(self, infile):
        self.userData = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID

    def __repr__(self):
        return "<{class_name} userData={userData}>".format(**{
            "class_name": self.__class__.__name__,
            "userData": self.userData,
        })
