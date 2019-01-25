from .hkpBallGun import hkpBallGun
from .common import vector4
import struct


class hkpMountedBallGun(hkpBallGun):
    position: vector4

    def __init__(self, infile):
        self.position = struct.unpack('>4f', infile.read(16))
