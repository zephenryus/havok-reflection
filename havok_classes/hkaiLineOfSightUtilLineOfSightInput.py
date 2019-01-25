from .hkaiLineOfSightUtilInputBase import hkaiLineOfSightUtilInputBase
import struct


class hkaiLineOfSightUtilLineOfSightInput(hkaiLineOfSightUtilInputBase):
    goalPoint: vector4
    goalFaceKey: int

    def __init__(self, infile):
        self.goalPoint = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.goalFaceKey = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} goalPoint={goalPoint}, goalFaceKey={goalFaceKey}>".format(**{
            "class_name": self.__class__.__name__,
            "goalPoint": self.goalPoint,
            "goalFaceKey": self.goalFaceKey,
        })
