from .hkpShapeBase import hkpShapeBase
import struct


class hkpShape(hkpShapeBase):
    userData: int

    def __init__(self, infile):
        self.userData = struct.unpack('>L', infile.read(8))
