from .hkpFirstPersonGun import hkpFirstPersonGun
from .common import any, vector4
import struct


class hkpGravityGun(hkpFirstPersonGun):
    grabbedBodies: any
    maxNumObjectsPicked: int
    maxMassOfObjectPicked: float
    maxDistOfObjectPicked: float
    impulseAppliedWhenObjectNotPicked: float
    throwVelocity: float
    capturedObjectPosition: vector4
    capturedObjectsOffset: vector4

    def __init__(self, infile):
        self.grabbedBodies = any(infile)  # TYPE_ARRAY
        self.maxNumObjectsPicked = struct.unpack('>i', infile.read(4))
        self.maxMassOfObjectPicked = struct.unpack('>f', infile.read(4))
        self.maxDistOfObjectPicked = struct.unpack('>f', infile.read(4))
        self.impulseAppliedWhenObjectNotPicked = struct.unpack('>f', infile.read(4))
        self.throwVelocity = struct.unpack('>f', infile.read(4))
        self.capturedObjectPosition = struct.unpack('>4f', infile.read(16))
        self.capturedObjectsOffset = struct.unpack('>4f', infile.read(16))
