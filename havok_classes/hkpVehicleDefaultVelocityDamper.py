from .hkpVehicleVelocityDamper import hkpVehicleVelocityDamper
import struct


class hkpVehicleDefaultVelocityDamper(hkpVehicleVelocityDamper):
    normalSpinDamping: float
    collisionSpinDamping: float
    collisionThreshold: float

    def __init__(self, infile):
        self.normalSpinDamping = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.collisionSpinDamping = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.collisionThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} normalSpinDamping={normalSpinDamping}, collisionSpinDamping={collisionSpinDamping}, collisionThreshold={collisionThreshold}>".format(**{
            "class_name": self.__class__.__name__,
            "normalSpinDamping": self.normalSpinDamping,
            "collisionSpinDamping": self.collisionSpinDamping,
            "collisionThreshold": self.collisionThreshold,
        })
