from .hkaiLineOfSightUtilInputBase import hkaiLineOfSightUtilInputBase
from .common import vector4
import struct


class hkaiLineOfSightUtilDirectPathInput(hkaiLineOfSightUtilInputBase):
    direction: vector4

    def __init__(self, infile):
        self.direction = struct.unpack('>4f', infile.read(16))
