from .hkaiLineOfSightUtilInputBase import hkaiLineOfSightUtilInputBase
from .common import vector4
import struct


class hkaiLineOfSightUtilLineOfSightInput(hkaiLineOfSightUtilInputBase):
    goalPoint: vector4
    goalFaceKey: int

    def __init__(self, infile):
        self.goalPoint = struct.unpack('>4f', infile.read(16))
        self.goalFaceKey = struct.unpack('>I', infile.read(4))
