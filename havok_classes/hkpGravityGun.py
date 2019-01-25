from .hkpFirstPersonGun import hkpFirstPersonGun
from typing import List
from .common import get_array
import struct


class hkpGravityGun(hkpFirstPersonGun):
    grabbedBodies: List[any]
    maxNumObjectsPicked: int
    maxMassOfObjectPicked: float
    maxDistOfObjectPicked: float
    impulseAppliedWhenObjectNotPicked: float
    throwVelocity: float
    capturedObjectPosition: vector4
    capturedObjectsOffset: vector4

    def __init__(self, infile):
        self.grabbedBodies = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.maxNumObjectsPicked = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.maxMassOfObjectPicked = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxDistOfObjectPicked = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.impulseAppliedWhenObjectNotPicked = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.throwVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.capturedObjectPosition = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.capturedObjectsOffset = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} grabbedBodies=[{grabbedBodies}], maxNumObjectsPicked={maxNumObjectsPicked}, maxMassOfObjectPicked={maxMassOfObjectPicked}, maxDistOfObjectPicked={maxDistOfObjectPicked}, impulseAppliedWhenObjectNotPicked={impulseAppliedWhenObjectNotPicked}, throwVelocity={throwVelocity}, capturedObjectPosition={capturedObjectPosition}, capturedObjectsOffset={capturedObjectsOffset}>".format(**{
            "class_name": self.__class__.__name__,
            "grabbedBodies": self.grabbedBodies,
            "maxNumObjectsPicked": self.maxNumObjectsPicked,
            "maxMassOfObjectPicked": self.maxMassOfObjectPicked,
            "maxDistOfObjectPicked": self.maxDistOfObjectPicked,
            "impulseAppliedWhenObjectNotPicked": self.impulseAppliedWhenObjectNotPicked,
            "throwVelocity": self.throwVelocity,
            "capturedObjectPosition": self.capturedObjectPosition,
            "capturedObjectsOffset": self.capturedObjectsOffset,
        })
