from .hkaiLineOfSightUtilInputBase import hkaiLineOfSightUtilInputBase
import struct


class hkaiLineOfSightUtilDirectPathInput(hkaiLineOfSightUtilInputBase):
    direction: vector4

    def __init__(self, infile):
        self.direction = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} direction={direction}>".format(**{
            "class_name": self.__class__.__name__,
            "direction": self.direction,
        })
