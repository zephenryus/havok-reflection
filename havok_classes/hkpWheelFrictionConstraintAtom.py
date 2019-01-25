from .hkpConstraintAtom import hkpConstraintAtom
import struct
from .hkpWheelFrictionConstraintAtomAxle import hkpWheelFrictionConstraintAtomAxle


class hkpWheelFrictionConstraintAtom(hkpConstraintAtom):
    isEnabled: int
    forwardAxis: int
    sideAxis: int
    radius: float
    axle: any
    maxFrictionForce: float
    torque: float
    frictionImpulse: float
    slipImpulse: float
    padding: int

    def __init__(self, infile):
        self.isEnabled = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.forwardAxis = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.sideAxis = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.radius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.axle = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.maxFrictionForce = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.torque = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.frictionImpulse = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.slipImpulse = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} isEnabled={isEnabled}, forwardAxis={forwardAxis}, sideAxis={sideAxis}, radius={radius}, axle={axle}, maxFrictionForce={maxFrictionForce}, torque={torque}, frictionImpulse={frictionImpulse}, slipImpulse={slipImpulse}, padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "isEnabled": self.isEnabled,
            "forwardAxis": self.forwardAxis,
            "sideAxis": self.sideAxis,
            "radius": self.radius,
            "axle": self.axle,
            "maxFrictionForce": self.maxFrictionForce,
            "torque": self.torque,
            "frictionImpulse": self.frictionImpulse,
            "slipImpulse": self.slipImpulse,
            "padding": self.padding,
        })
