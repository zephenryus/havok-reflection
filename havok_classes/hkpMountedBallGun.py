from .hkpBallGun import hkpBallGun
import struct


class hkpMountedBallGun(hkpBallGun):
    position: vector4

    def __init__(self, infile):
        self.position = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} position={position}>".format(**{
            "class_name": self.__class__.__name__,
            "position": self.position,
        })
