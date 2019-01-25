from .hkpFirstPersonGun import hkpFirstPersonGun
import struct


class hkpBallGun(hkpFirstPersonGun):
    bulletRadius: float
    bulletVelocity: float
    bulletMass: float
    damageMultiplier: float
    maxBulletsInWorld: int
    bulletOffsetFromCenter: vector4
    addedBodies: any

    def __init__(self, infile):
        self.bulletRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.bulletVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.bulletMass = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.damageMultiplier = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxBulletsInWorld = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.bulletOffsetFromCenter = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.addedBodies = any(infile)  # TYPE_POINTER:TYPE_VOID

    def __repr__(self):
        return "<{class_name} bulletRadius={bulletRadius}, bulletVelocity={bulletVelocity}, bulletMass={bulletMass}, damageMultiplier={damageMultiplier}, maxBulletsInWorld={maxBulletsInWorld}, bulletOffsetFromCenter={bulletOffsetFromCenter}, addedBodies={addedBodies}>".format(**{
            "class_name": self.__class__.__name__,
            "bulletRadius": self.bulletRadius,
            "bulletVelocity": self.bulletVelocity,
            "bulletMass": self.bulletMass,
            "damageMultiplier": self.damageMultiplier,
            "maxBulletsInWorld": self.maxBulletsInWorld,
            "bulletOffsetFromCenter": self.bulletOffsetFromCenter,
            "addedBodies": self.addedBodies,
        })
