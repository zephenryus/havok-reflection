from .hkpWheelFrictionConstraintAtomAxle import hkpWheelFrictionConstraintAtomAxle
from .hkpWheelFrictionConstraintData import hkpWheelFrictionConstraintData
import struct


class hkpVehiclePerWheelSimulationWheelData(object):
    axle: hkpWheelFrictionConstraintAtomAxle
    frictionData: hkpWheelFrictionConstraintData
    frictionConstraint: any
    forwardDirectionWs: vector4
    sideDirectionWs: vector4
    contactLocal: vector4

    def __init__(self, infile):
        self.axle = hkpWheelFrictionConstraintAtomAxle(infile)  # TYPE_STRUCT:TYPE_VOID
        self.frictionData = hkpWheelFrictionConstraintData(infile)  # TYPE_STRUCT:TYPE_VOID
        self.frictionConstraint = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.forwardDirectionWs = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.sideDirectionWs = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.contactLocal = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} axle={axle}, frictionData={frictionData}, frictionConstraint={frictionConstraint}, forwardDirectionWs={forwardDirectionWs}, sideDirectionWs={sideDirectionWs}, contactLocal={contactLocal}>".format(**{
            "class_name": self.__class__.__name__,
            "axle": self.axle,
            "frictionData": self.frictionData,
            "frictionConstraint": self.frictionConstraint,
            "forwardDirectionWs": self.forwardDirectionWs,
            "sideDirectionWs": self.sideDirectionWs,
            "contactLocal": self.contactLocal,
        })
