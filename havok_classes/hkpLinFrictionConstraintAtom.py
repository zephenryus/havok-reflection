from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpLinFrictionConstraintAtom(hkpConstraintAtom):
    isEnabled: int
    frictionAxis: int
    maxFrictionForce: float
    padding: int

    def __init__(self, infile):
        self.isEnabled = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.frictionAxis = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.maxFrictionForce = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} isEnabled={isEnabled}, frictionAxis={frictionAxis}, maxFrictionForce={maxFrictionForce}, padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "isEnabled": self.isEnabled,
            "frictionAxis": self.frictionAxis,
            "maxFrictionForce": self.maxFrictionForce,
            "padding": self.padding,
        })
