from .hkpFirstPersonGun import hkpFirstPersonGun
import struct
from .common import vector4, any


class hkpBallGun(hkpFirstPersonGun):
    bulletRadius: float
    bulletVelocity: float
    bulletMass: float
    damageMultiplier: float
    maxBulletsInWorld: int
    bulletOffsetFromCenter: vector4
    addedBodies: any

    def __init__(self, infile):
        self.bulletRadius = struct.unpack('>f', infile.read(4))
        self.bulletVelocity = struct.unpack('>f', infile.read(4))
        self.bulletMass = struct.unpack('>f', infile.read(4))
        self.damageMultiplier = struct.unpack('>f', infile.read(4))
        self.maxBulletsInWorld = struct.unpack('>i', infile.read(4))
        self.bulletOffsetFromCenter = struct.unpack('>4f', infile.read(16))
        self.addedBodies = any(infile)  # TYPE_POINTER
