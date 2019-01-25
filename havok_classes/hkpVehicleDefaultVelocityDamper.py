from .hkpVehicleVelocityDamper import hkpVehicleVelocityDamper
import struct


class hkpVehicleDefaultVelocityDamper(hkpVehicleVelocityDamper):
    normalSpinDamping: float
    collisionSpinDamping: float
    collisionThreshold: float

    def __init__(self, infile):
        self.normalSpinDamping = struct.unpack('>f', infile.read(4))
        self.collisionSpinDamping = struct.unpack('>f', infile.read(4))
        self.collisionThreshold = struct.unpack('>f', infile.read(4))
