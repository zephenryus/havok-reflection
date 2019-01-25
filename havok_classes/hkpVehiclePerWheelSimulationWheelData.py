from .hkpWheelFrictionConstraintAtomAxle import hkpWheelFrictionConstraintAtomAxle
from .hkpWheelFrictionConstraintData import hkpWheelFrictionConstraintData
from .common import any, vector4
import struct


class hkpVehiclePerWheelSimulationWheelData(object):
    axle: hkpWheelFrictionConstraintAtomAxle
    frictionData: hkpWheelFrictionConstraintData
    frictionConstraint: any
    forwardDirectionWs: vector4
    sideDirectionWs: vector4
    contactLocal: vector4

    def __init__(self, infile):
        self.axle = hkpWheelFrictionConstraintAtomAxle(infile)  # TYPE_STRUCT
        self.frictionData = hkpWheelFrictionConstraintData(infile)  # TYPE_STRUCT
        self.frictionConstraint = any(infile)  # TYPE_POINTER
        self.forwardDirectionWs = struct.unpack('>4f', infile.read(16))
        self.sideDirectionWs = struct.unpack('>4f', infile.read(16))
        self.contactLocal = struct.unpack('>4f', infile.read(16))
